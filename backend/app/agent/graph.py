from langgraph.graph import StateGraph, END
from .state import State
from .nodes import router,normal_chat,generate_sql_answer,rag_chat,generate_query,run_query

workflow = StateGraph(State)

workflow.add_node("router", router)
workflow.add_node("normal_chat", normal_chat)
workflow.add_node("generate_query", generate_query)
workflow.add_node("run_query", run_query)
workflow.add_node("generate_sql_answer", generate_sql_answer)
workflow.add_node("rag_chat", rag_chat)

workflow.set_entry_point("router")


def route_condition(state):
    return state["route"]


workflow.add_conditional_edges(
    "router",
    route_condition,
    {
        "sql": "generate_query",
        "chat": "normal_chat",
        "rag": "rag_chat"
    }
)


workflow.add_edge("normal_chat", END)

workflow.add_edge("generate_query", "run_query")
workflow.add_edge("run_query", "generate_sql_answer")
workflow.add_edge("generate_sql_answer", END)

workflow.add_edge("rag_chat", END)

app_workflow = workflow.compile()