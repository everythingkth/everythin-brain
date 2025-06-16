# vector_config.py

VECTOR_DB_CONFIG = {
    "provider": "weaviate",
    "host": "https://your-weaviate-instance.weaviate.network",  # 여기에 본인 벡터 DB 주소 입력
    "api_key": "your_weaviate_api_key"  # 여기에 발급받은 API 키 입력
}

EMBEDDING_MODEL = "text-embedding-ada-002"  # OpenAI 임베딩 모델
