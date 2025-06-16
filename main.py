from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage

app = FastAPI()

# 환경 변수에서 OpenAI API 키 가져오기
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 벡터 저장소 로딩
PERSIST_DIR = "./storage"
if os.path.exists(PERSIST_DIR):
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
else:
    documents = SimpleDirectoryReader("./data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist()

# 쿼리 API용 클래스
class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_data(request: QueryRequest):
    query_engine = index.as_query_engine()
    response = query_engine.query(request.question)
    return {"response": str(response)}
