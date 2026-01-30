from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import get_response

app = FastAPI(title="Restaurant Chatbot API")


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    reply = get_response(req.message)
    return {"reply": reply}