from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import GEMINI_API_KEY

def get_llm():
    return ChatGoogleGenerativeAI(
        # model="gemini-2.5-flash",
        # model="gemini-2.5-flash-lite",
        model="gemini-3-flash-preview",
        # model="gemini-3.1-flash-lite-preview",
        temperature=0.3,
        api_key=GEMINI_API_KEY,
    )