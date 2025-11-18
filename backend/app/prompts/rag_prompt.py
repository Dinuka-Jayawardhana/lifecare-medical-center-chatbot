from langchain_core.prompts import PromptTemplate

rag_prompt = PromptTemplate.from_template("""
Answer this question using ONLY the context below.
                                          
When answering:
- Be clear, natural, and a bit creative.
- If the context contains only one key fact, present it smoothly in a nice sentence.
- If there are multiple details, organize them in a clean, readable format.
- Keep the tone warm, human, and easy to understand.

Question:
{question}

Context:
{context}

Answer:
""")