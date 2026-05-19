from fastapi import FastAPI
from pydantic import BaseModel
from utils.rag_utils import load_chunks, get_embeddings, retrieve
import requests
from utils.vector_store import (create_index)
from schemas.chat import (ChatRequest, ChatResponse)

app = FastAPI()

# Load chunks
chunks = load_chunks()

# Generate embeddings
embeddings = get_embeddings(chunks)

# Create FAISS index
index = create_index(embeddings)

@app.post("/ask", response_model=ChatResponse)
def ask(req: ChatRequest):

    # Retrieve relevant chunks
    relevant_chunks = retrieve(req.message, chunks, index, k=3)

    context = "\n".join(relevant_chunks)

    
    # Call LLM
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2:3b",
            "messages": [
                {
                    "role": "system",
                    "content": """
                    You are a question-answering system.

                    Use ONLY the provided context.

                    If answer is not present, say:
                    'I don't know based on the provided context.'

                    Be concise and accurate.
                    """
                },
                {
                    "role": "user",
                    "content": f"""
                            Use the context below to answer the question.
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

    return ChatResponse(
    response=response.json()["message"]["content"],
    context_used=relevant_chunks
    )