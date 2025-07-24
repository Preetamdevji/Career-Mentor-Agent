from config import GEMINI_API_KEY, GENAI_BASE_URL
from openai import AsyncOpenAI

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GENAI_BASE_URL
)

def call_gemini(prompt):
     pass