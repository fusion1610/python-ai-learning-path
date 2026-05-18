from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text, chunk_size=40, overlap=10):
    words=text.split()
    chunks=[]
    for i in range(0, len(words), chunk_size - overlap):
        chunk = words[i: i + chunk_size]
        chunks.append(" ".join(chunk))

    return chunks

def load_chunks():
    with open("data/data.txt") as f:
        text = f.read()

    return chunk_text(text)

def get_embeddings(chunks):
    return model.encode(chunks)

def retrieve(query, chunks, embeddings, k=3):
    query_embedding = model.encode([query])

    scores = cosine_similarity(query_embedding, embeddings)[0]

    print(scores)

    # get top 2 chunks
    top_indices = scores.argsort()[-k:][::-1]

    return [chunks[i] for i in top_indices]