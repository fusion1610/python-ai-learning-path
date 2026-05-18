import requests

from app.utils.rag_utils import (
    load_chunks,
    get_embeddings,
    retrieve
)

# Load chunks
chunks = load_chunks()

print("\n===== CHUNKS =====")
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)

# Generate embeddings
embeddings = get_embeddings(chunks)

# User query
query = "Why is FastAPI good for AI systems?"

# Retrieve relevant chunks
relevant_chunks = retrieve(
    query,
    chunks,
    embeddings,
    k=3
)

print("\n===== RETRIEVED CHUNKS =====")
for chunk in relevant_chunks:
    print("-", chunk)

# Create context
context = "\n".join(relevant_chunks)

# Send to Ollama
response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "llama3.2:3b",
        "messages": [
            {
                "role": "system",
                "content": """
You are a question-answering AI system.

Answer ONLY from the provided context.

If answer is not available in context, say:
'I don't know based on the provided context.'

Be concise and accurate.
"""
            },
            {
                "role": "user",
                "content": f"""
Context:
{context}

Question:
{query}
"""
            }
        ],
        "stream": False
    }
)

# Print response
print("\n===== AI RESPONSE =====")
print(response.json()["message"]["content"])