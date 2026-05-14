from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.post("/chat")
def chat(req: ChatRequest):

    last_messages = req.messages[-5:]

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2:3b",
            "messages": [
                {"role": "system", "content": "You are a helpful AI assistant"}
            ] + [m.model_dump() for m in last_messages],
            "stream": False
        }
    )

    return {
        "response": response.json()["message"]["content"],
        "messages": req.messages
    }