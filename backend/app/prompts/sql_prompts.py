from langchain_core.prompts import PromptTemplate

query_prompt = PromptTemplate.from_template("""
You are an expert SQL generator for a hospital database.
Use **only these tables and columns**:
{schema}
                                                                            
Generate ONLY the SQL query. No explanation.

User Question: {question}

SQL Query:
""")