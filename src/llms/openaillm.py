from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

class OpenaiLlm:
    def __init__(self):
        load_dotenv()
        self.open_api_key = os.getenv("OPENAI_API_KEY")

        if not self.open_api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")

    def get_llm(self):
        try:
            # Optional: print only for debugging (remove in production)
            # print(self.open_api_key)

            llm = ChatOpenAI(
                api_key=self.open_api_key,
                model="gpt-4o-mini",
                temperature=0.7
            )
            return llm

        except Exception as e:
            raise ValueError(f"Error occurred: {e}")
