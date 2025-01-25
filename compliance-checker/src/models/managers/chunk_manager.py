class ChunkManager:
    def split_text(self, text: str, chunk_size: int, overlap: int) -> list:
        """
        Splits text into smaller overlapping chunks.

        Args:
            text (str): The text to split.
            chunk_size (int): Size of each chunk in characters.
            overlap (int): Number of overlapping characters between chunks.

        Returns:
            list: List of text chunks.
        """
        if not text or chunk_size <= 0 or overlap < 0:
            raise ValueError("Invalid input parameters for chunking.")

        chunks = []
        start = 0
        
        # Create overlapping chunks
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunks.append(text[start:end])
            start += chunk_size - overlap  # Move start forward by chunk_size minus overlap
        
        return chunks
