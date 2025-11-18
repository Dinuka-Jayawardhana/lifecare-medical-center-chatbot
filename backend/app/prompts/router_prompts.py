from langchain_core.prompts import PromptTemplate

route_prompt = PromptTemplate.from_template("""
Classify the user question.

User Question: {question}

Respond with exactly one word:
- "sql"  → if the question requires a database lookup
- "rag"  → if the question requires document retrieval
- "chat" → if the question is a normal conversation

Answer:
""")
