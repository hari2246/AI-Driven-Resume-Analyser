from fastapi import APIRouter, UploadFile, HTTPException
from managers.pdf_manager import PDFManager

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile):
    """
    API endpoint to upload a PDF file and validate it.

    Args:
        file (UploadFile): The uploaded file.

    Returns:
        dict: A response message and file path.
    """
    try:
        # Initialize the manager
        manager = PDFManager()

        # Validate and save the PDF
        saved_path = await manager.validate_and_save_pdf(file)

        return {"message": "PDF successfully uploaded", "file_path": saved_path}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload PDF: {str(e)}")
