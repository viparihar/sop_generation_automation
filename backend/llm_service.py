import os

from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI

from .prompts import sop_prompt

from .models import SOPModel

load_dotenv()

llm = ChatMistralAI(
    model = "mistral-small-2603",
    api_key = os.getenv("MISTRAL_API_KEY")
)

structured_llm = llm.with_structured_output(
    SOPModel
)

chain = sop_prompt | structured_llm


class SOPService:

    @staticmethod
    def generate_sop(transcript: str):

        return chain.invoke(
            {
                "transcript": transcript
            }
        )