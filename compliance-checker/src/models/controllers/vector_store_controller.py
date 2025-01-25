from fastapi import APIRouter, HTTPException
from managers.vector_store_manager import VectorStoreManager

# Initialize router
router = APIRouter()

@router.post("/store-embeddings/")
async def store_embeddings(embeddings: list, namespace: str = "default"):
    """
    API to store embeddings in a hosted vector database.

    Args:
        embeddings (list): List of embeddings to store.
        namespace (str): Namespace for the embeddings.

    Returns:
        dict: Confirmation of storage.
    """
    try:
        # Initialize VectorStoreManager
        manager = VectorStoreManager()

        # Store embeddings
        manager.store_embeddings(embeddings, namespace)
        return {"message": "Embeddings stored successfully", "namespace": namespace}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to store embeddings: {str(e)}")


@router.get("/search-embeddings/")
async def search_embeddings(query_embedding: list, namespace: str = "default", k: int = 5):
    """
    API to search for the top-k nearest neighbors in the hosted vector database.

    Args:
        query_embedding (list): The embedding to search for.
        namespace (str): Namespace to search in.
        k (int): Number of nearest neighbors to retrieve.

    Returns:
        dict: Nearest neighbors and their distances.
    """
    try:
        # Initialize VectorStoreManager
        manager = VectorStoreManager()

        # Perform search
        results = manager.search_embeddings(query_embedding, namespace, k)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to search embeddings: {str(e)}")
