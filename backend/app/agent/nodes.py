from .state import State
from .llm import llm
from app.prompts import *
from langchain_core.output_parsers import StrOutputParser
from pydantic import ValidationError
from langchain_core.runnables import RunnablePassthrough
from app.rag.pdf_retriever import create_pdf_retriever
from app.utils import *
from app.validations import *
from app.db.DBConnection import SessionLocal
from sqlalchemy import text



def generate_query(state: State):
    try:
        state_with_schema = state.copy()
        state_with_schema["schema"] = schema_info

        query = (query_prompt | llm | StrOutputParser()).invoke(state_with_schema)

        SQLQueryModel(query=query)
        return {"query": query}

    except ValidationError as e:
        return {"query": f"INVALID: {e}"}
    


def run_query(state: State):
    try:
        SQLQueryModel(query=state["query"])

        session = SessionLocal()
        try:
            result = session.execute(text(state["query"])).fetchall()
            result_dicts = [dict(row._mapping) for row in result]
        finally:
            session.close()

        SQLResultModel(result=result_dicts)
        return {"result": result_dicts}

    except ValidationError as e:
        return {"result": f"INVALID: {e}"}
    


def generate_sql_answer(state: State):
    answer = (sql_answer_prompt | llm | StrOutputParser()).invoke(state)
    return {"answer": answer}


def router(state: State):
    decision = (route_prompt | llm | StrOutputParser()).invoke(state).strip().lower()
    return {"route": decision}


def normal_chat(state: State):
        answer = (normal_chat_prompt | llm | StrOutputParser()).invoke(state)
        return {"answer": answer}


retriever = create_pdf_retriever()


def rag_chat(state: State):
        question = state["question"]

        rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | rag_prompt
            | llm
            | StrOutputParser()
        )

        answer = rag_chain.invoke(question)
        return {"answer": answer}