from fastapi import FastAPI
from pydantic import BaseModel
from utils.rag_utils import load_chunks, get_embeddings, retrieve
import requests

app = FastAPI()

# Load once (IMPORTANT)
chunks = load_chunks()
embeddings = get_embeddings(chunks)

class ChatRequest(BaseModel):
    message: str

@app.post("/ask")
def ask(req: ChatRequest):

    # Retrieve relevant chunks
    relevant_chunks = retrieve(req.message, chunks, embeddings)

    context = "\n".join(relevant_chunks)

    
    # Call LLM
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2:3b",
            "messages": [
                {
                    "role": "system",
                    "content": "Answer ONLY using the provided context"
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
            ],
            "stream": False
        }
    )

    return {
        "response": response.json()["message"]["content"],
        "context_used": relevant_chunks
    }