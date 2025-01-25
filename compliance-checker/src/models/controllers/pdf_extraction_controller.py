from fastapi import APIRouter, UploadFile, HTTPException
from managers.pdf_extraction_manager import PDFExtractionManager

router = APIRouter()

@router.post("/extract-text/")
async def extract_text(file: UploadFile):
    """
    API endpoint to extract text from a PDF file.

    Args:
        file (UploadFile): The uploaded PDF file.

    Returns:
        dict: Extracted text or an error message.
    """
    manager = PDFExtractionManager()

    try:
        # Save the temporary file
        temp_file_path = await manager.save_temp_file(file)
        
        # Extract text from the PDF
        extracted_text = manager.extract_text_from_pdf(temp_file_path)
        
        return {"message": "Text successfully extracted", "extracted_text": extracted_text}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to extract text: {str(e)}")
    finally:
        # Cleanup temporary file
        manager.cleanup_temp_file(temp_file_path)
