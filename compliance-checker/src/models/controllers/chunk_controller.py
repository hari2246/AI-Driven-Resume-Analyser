from fastapi import APIRouter, HTTPException
from managers.chunk_manager import ChunkManager

# Initialize router
router = APIRouter()

@router.post("/chunk/")
async def chunk_text(extracted_text: str, chunk_size: int, overlap: int):
    """
    API to split the extracted text into smaller overlapping chunks.

    Args:
        extracted_text (str): The input text to chunk.
        chunk_size (int): Size of each chunk in characters.
        overlap (int): Number of overlapping characters between chunks.

    Returns:
        dict: Chunks of text.
    """
    try:
        # Initialize ChunkManager
        manager = ChunkManager()
        
        # Generate chunks
        chunks = manager.split_text(extracted_text, chunk_size, overlap)
        return {"chunks": chunks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to chunk text: {str(e)}")
