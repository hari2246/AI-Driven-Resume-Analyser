# src/utils/vector_store_pinecone.py

import pinecone
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class PineconeVectorStore:
    def __init__(self, index_name: str):
        # Load Pinecone API key and environment from environment variables
        pinecone_api_key = os.getenv("PINECONE_API_KEY")
        pinecone_env = os.getenv("PINECONE_ENVIRONMENT")
        
        if not pinecone_api_key or not pinecone_env:
            raise ValueError("Pinecone API key or environment not set in .env file.")
        
        # Initialize Pinecone
        pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)
        
        # Create or connect to the index
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(index_name, dimension=384)  # Match dimension to embeddings
        self.index = pinecone.Index(index_name)
    
    def add_embeddings(self, ids: list, embeddings: list):
        """Add embeddings to Pinecone."""
        self.index.upsert(vectors=zip(ids, embeddings))
    
    def search(self, query_vector: list, top_k: int = 5):
        """Search for similar embeddings."""
        return self.index.query(vector=query_vector, top_k=top_k, include_metadata=True)
