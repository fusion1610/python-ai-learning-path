import requests
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model (Hugging Face)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 1: Load data
with open("app/data/data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Step 2: Chunk data (simple line-based)
chunks = [line.strip() for line in text.split("\n") if line.strip()]

# Step 3: Generate embeddings
embeddings = model.encode(chunks)

# Step 4: User query
query = "Why is FastAPI popular?"

# Step 5: Convert query to embedding
query_embedding = model.encode([query])

# Step 6: Similarity search
scores = cosine_similarity(query_embedding, embeddings)[0]

# Get top 2 relevant chunks
top_indices = scores.argsort()[-2:][::-1]
relevant_chunks = [chunks[i] for i in top_indices]

print("Relevant chunks:")
for chunk in relevant_chunks:
    print("-", chunk)

# Step 7: Create context
context = "\n".join(relevant_chunks)



url = "http://localhost:11434/api/chat"

# Step 8: Send to Ollama
response = requests.post(url,
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
                    {query}
                    """
            }
        ],
        "stream": False
        }
    )

# Step 9: Print response
print("\nAI Response:")
print(response.json()["message"]["content"])