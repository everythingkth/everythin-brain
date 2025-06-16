from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str, model: str = "text-embedding-3-small") -> list:
    response = client.embeddings.create(
        input=[text],
        model=model
    )
    return response.data[0].embedding
