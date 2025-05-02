import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()

def run_agent(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Missing OpenAI API key."

    llm = ChatOpenAI(openai_api_key=api_key, temperature=0.7)
    return llm.predict(prompt)

