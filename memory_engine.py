# memory_engine.py

import openai
from vector_config import VECTOR_DB_CONFIG, EMBEDDING_MODEL

# ✅ GPT API 키 설정 (렌더에서 환경변수로 관리할 예정)
openai.api_key = "your_openai_api_key"

def embed_text(text):
    """텍스트를 벡터로 변환"""
    response = openai.Embedding.create(
        input=text,
        model=EMBEDDING_MODEL
    )
    return response['data'][0]['embedding']

def store_to_vector_db(text, metadata=None):
    """벡터 DB에 텍스트 저장"""
    embedding = embed_text(text)

    # 여기에 벡터 DB 저장 로직 구현 예정
    # 예: Weaviate, Pinecone 등

    print("✅ 저장 완료 (모의):", text[:30], "...")

def search_from_vector_db(query):
    """벡터 DB에서 관련 내용 검색"""
    query_vector = embed_text(query)

    # 벡터 DB에서 유사도 검색 로직 구현 예정
    # 예: 가장 유사한 top-k 반환

    print("🔍 검색 완료 (모의):", query)
    return ["(예시) 검색 결과 1", "(예시) 검색 결과 2"]
