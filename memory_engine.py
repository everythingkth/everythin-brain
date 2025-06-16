import os
from openai import OpenAI
import numpy as np
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EMBEDDING_MODEL = "text-embedding-ada-002"

# 🔹 텍스트 임베딩
def embed_text(text):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=[text]
    )
    return response.data[0].embedding

# 🔹 메모리 DB (예시: 로컬 리스트)
memory_db = []

# 🔹 벡터 저장
def store_to_vector_db(content, vector):
    memory_db.append({"content": content, "vector": np.array(vector)})

# 🔹 벡터 검색 (유사도 기반)
def search_from_vector_db(query_vector, top_k=3):
    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    results = [
        {
            "content": item["content"],
            "score": cosine_similarity(query_vector, item["vector"])
        }
        for item in memory_db
    ]
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]
