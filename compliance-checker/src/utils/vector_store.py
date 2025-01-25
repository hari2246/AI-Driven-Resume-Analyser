import faiss
import numpy as np

class LocalVectorStore:
    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.embeddings = []
    
    def add_embeddings(self, embeddings: list):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
    
    def search(self, query_vector: list, top_k: int = 5):
        query = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query, top_k)
        return distances, indices
