import requests

from sentence_transformers import SentenceTransformer

from app.utils.rag_utils import (
    load_chunks,
    get_embeddings,
    retrieve
)

from app.utils.vector_store import (
    create_index
)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load chunks
chunks = load_chunks()

print("\n===== CHUNKS =====")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)

# Generate embeddings
embeddings = get_embeddings(chunks)

print("\n===== EMBEDDINGS GENERATED =====")
print(f"Total embeddings: {len(embeddings)}")

# Create FAISS index
index = create_index(embeddings)

print("\n===== FAISS INDEX CREATED =====")

# User query
query = "Why is FastAPI useful for AI applications?"

print("\n===== USER QUERY =====")
print(query)

# Retrieve relevant chunks using FAISS
relevant_chunks = retrieve(
    query=query,
    chunks=chunks,
    index=index,
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
                    You are a question-answering AI assistant.

                    Use ONLY the provided context.

                    If the answer is not present in the context, say:
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

# Print AI response
print("\n===== AI RESPONSE =====")
print(response.json()["message"]["content"])