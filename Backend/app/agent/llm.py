import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-5-nano",
    api_key=OPENAI_API_KEY,
    temperature=0
)
