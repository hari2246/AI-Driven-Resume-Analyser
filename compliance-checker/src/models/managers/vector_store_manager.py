import pinecone

class VectorStoreManager:
    def __init__(self, api_key: str, environment: str, index_name: str):
        """
        Initialize the VectorStoreManager with Pinecone credentials.
        """
        self.index_name = index_name

        # Initialize Pinecone
        pinecone.init(api_key=api_key, environment=environment)

        # Create the index if it does not exist
        if self.index_name not in pinecone.list_indexes():
            pinecone.create_index(self.index_name, dimension=1536)  # Set dimension based on embeddings

        # Connect to the index
        self.index = pinecone.Index(self.index_name)

    def store_embeddings(self, embeddings: list, namespace: str):
        """
        Store embeddings in the Pinecone vector database.

        Args:
            embeddings (list): List of embeddings to store.
            namespace (str): Namespace for the embeddings.
        """
        # Prepare the data for Pinecone
        vectors = [(str(i), embedding) for i, embedding in enumerate(embeddings)]
        
        # Upsert data into the index
        self.index.upsert(vectors, namespace=namespace)

    def search_embeddings(self, query_embedding: list, namespace: str, k: int) -> list:
        """
        Search for the top-k nearest neighbors in the Pinecone vector database.

        Args:
            query_embedding (list): The embedding to search for.
            namespace (str): Namespace to search in.
            k (int): Number of nearest neighbors to retrieve.

        Returns:
            list: Nearest neighbors and their distances.
        """
        # Perform the search
        results = self.index.query(query_embedding, top_k=k, namespace=namespace, include_metadata=False)

        # Format results
        return [{"id": match["id"], "score": match["score"]} for match in results["matches"]]
