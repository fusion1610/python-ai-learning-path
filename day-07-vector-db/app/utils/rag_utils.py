from sentence_transformers import SentenceTransformer
from utils.vector_store import (search_index)

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

def retrieve(query, chunks,index, k=3):
    query_embedding = model.encode([query])

    indices = search_index(index, query_embedding, k)

    print(indices)

    return [chunks[i] for i in indices]