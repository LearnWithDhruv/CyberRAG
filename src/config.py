import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    CHROMA_PATH = os.getenv("CHROMA_PATH")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config = Config()
