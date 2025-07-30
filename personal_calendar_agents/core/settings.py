import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings:

    def __init__(self):
        load_dotenv()
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
        self.GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "")
        self.credentials_json = os.path.join(BASE_DIR, os.getenv('GOOGLE_CREDENTIALS_JSON'))
        self.credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH')
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


settings = Settings()

# print(os.path.exists(settings.credentials_json))
