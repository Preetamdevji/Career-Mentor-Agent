from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GENAI_BASE_URL = os.getenv("GENAI_BASE_URL")
