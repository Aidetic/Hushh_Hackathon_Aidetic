import os
from dotenv import load_dotenv

class Settings:

    def __init__(self):
        load_dotenv()
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
        self.GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "")
        self.credentials_json = os.getenv('GOOGLE_CREDENTIALS_JSON')
        self.credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH')


settings = Settings()

print(os.path.exists(settings.credentials_json))
