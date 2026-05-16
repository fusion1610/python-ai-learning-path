from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_chunks():
    with open("data/data.txt") as f:
        text = f.read()

    # simple chunking (line-based)
    chunks = [line.strip() for line in text.split("\n") if line.strip()]

    return chunks

def get_embeddings(chunks):
    return model.encode(chunks)

def retrieve(query, chunks, embeddings):
    query_embedding = model.encode([query])

    scores = cosine_similarity(query_embedding, embeddings)[0]

    # get top 2 chunks
    top_indices = scores.argsort()[-2:][::-1]

    return [chunks[i] for i in top_indices]