from sentence_transformers import SentenceTransformer

class EmbeddingManager:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the EmbeddingManager with a pre-trained model.
        """
        self.model = SentenceTransformer(model_name)
    
    async def create_embeddings(self, chunks: list) -> list:
        """
        Generate embeddings for a list of text chunks.

        Args:
            chunks (list): List of text chunks.

        Returns:
            list: List of embeddings for the text chunks.
        """
        if not chunks or not isinstance(chunks, list):
            raise ValueError("Chunks must be a non-empty list.")

        # Generate embeddings using the m
