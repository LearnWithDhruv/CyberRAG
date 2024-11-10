import openai
from src.config import config

class ResponseGenerator:
    def __init__(self):
        openai.api_key = config.OPENAI_API_KEY
    
    def generate_response(self, context, query):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Context: {context}\nQuery: {query}\nAnswer:",
            max_tokens=150
        )
        return response["choices"][0]["text"].strip()
