import os
from PyPDF2 import PdfReader
from fastapi import UploadFile

class PDFExtractionManager:
    def __init__(self, temp_dir: str = "./temp_files"):
        """
        Initialize the PDFExtractionManager with a temporary directory.
        """
        self.temp_dir = temp_dir
        os.makedirs(self.temp_dir, exist_ok=True)  # Create directory if it doesn't exist

    async def save_temp_file(self, file: UploadFile) -> str:
        """
        Save the uploaded PDF file temporarily for processing.

        Args:
            file (UploadFile): The uploaded file object.

        Returns:
            str: Path of the saved temporary file.
        """
        temp_file_path = os.path.join(self.temp_dir, file.filename)
        try:
            with open(temp_file_path, "wb") as f:
                f.write(await file.read())
        except Exception as e:
            raise RuntimeError(f"Failed to save temporary file: {str(e)}")
        
        return temp_file_path

    def extract_text_from_pdf(self, file_path: str) -> str:
        """
        Extract text from the PDF file and handle edge cases.

        Args:
            file_path (str): Path of the PDF file.

        Returns:
            str: Extracted text from the PDF.
        """
        try:
            # Read the PDF
            reader = PdfReader(file_path)
            extracted_text = ""
            for page in reader.pages:
                extracted_text += page.extract_text() or ""  # Handle missing text
            
            if not extracted_text.strip():
                raise ValueError("The PDF file contains no extractable text.")
            
            return extracted_text
        
        except Exception as e:
            raise RuntimeError(f"Failed to extract text: {str(e)}")

    def cleanup_temp_file(self, file_path: str):
        """
        Remove the temporary file after processing.

        Args:
            file_path (str): Path of the temporary file.
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Failed to remove temporary file: {str(e)}")
