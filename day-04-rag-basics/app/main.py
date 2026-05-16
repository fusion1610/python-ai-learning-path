from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/ask")
def ask(req: ChatRequest):

    # Load context (your custom data)
    with open("data.txt", "r", encoding="utf-8") as f:
        context = f.read()

    # Prepare messages for LLM    
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Answer ONLY from the provided context. If answer is not in context, say you don't know."
        },
        {
            "role": "user",
            "content": f"""
                    Context:
                    {context}

                    Question:
                    {req.message}
                    """
        }
    ]
    
    # Call Ollama
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2:3b",
            "messages": messages,
            "stream": False
        }
    )

    # Extract response
    result = response.json()["message"]["content"]

    return {
        "response": result
    }