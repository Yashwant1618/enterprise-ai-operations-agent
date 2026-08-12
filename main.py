from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import generate_answer


app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Enterprise AI Operations Agent is running"
    }


@app.post("/ask")
def ask_question(request: Question):
    answer = generate_answer(request.question)

    return {
        "question": request.question,
        "answer": answer
    }