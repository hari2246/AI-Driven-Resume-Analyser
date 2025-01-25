import os
from fastapi import UploadFile

class PDFManager:
    def __init__(self, upload_dir: str = "./uploaded_files"):
        """
        Initialize the PDFManager with an upload directory.
        """
        self.upload_dir = upload_dir
        os.makedirs(self.upload_dir, exist_ok=True)  # Create directory if it doesn't exist

    async def validate_and_save_pdf(self, file: UploadFile) -> str:
        """
        Validate the uploaded file as a PDF and save it.

        Args:
            file (UploadFile): The uploaded file object.

        Returns:
            str: Path where the file is saved.
        """
        # Validate the file type
        if file.content_type != "application/pdf":
            raise ValueError("Only PDF files are allowed.")
        
        # Save the file
        file_path = os.path.join(self.upload_dir, file.filename)
        try:
            with open(file_path, "wb") as f:
                f.write(await file.read())
        except Exception as e:
            raise RuntimeError(f"Failed to save file: {str(e)}")
        
        return file_path
