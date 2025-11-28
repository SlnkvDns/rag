from fastapi import FastAPI
from pydantic import BaseModel

from llm.llm import LLM   


llm = LLM(
    num_bm25_docs=10,
    num_faiss_docs=10,
    top_n=5,
    think=None
)

app = FastAPI(title="LLM API")


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str


@app.post("/generate", response_model=QueryResponse)
def generate_answer(request: QueryRequest):
    answer = llm.generate_answer(request.query)
    return QueryResponse(answer=answer)
