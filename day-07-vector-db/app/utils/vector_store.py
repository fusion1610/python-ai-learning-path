import faiss
import numpy as np

# Create FAISS index
def create_index(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))

    return index

def search_index(index, query_embedding, k=3):

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    return indices[0]