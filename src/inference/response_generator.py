import openai
from src.config import config

class ResponseGenerator:
    def __init__(self):
        openai.api_key = config.OPENAI_API_KEY
    
    def generate_response(self, context, query, model="gpt-3.5-turbo"):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides answers based on cybersecurity context."},
                {"role": "user", "content": f"Context: {context}\nQuery: {query}\nAnswer:"}
            ],
            max_tokens=150
        )
        return response["choices"][0]["message"]["content"].strip()
