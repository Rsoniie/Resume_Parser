# Extracting texts from docx file format
from docx import Document

__all__ = ["extract_text_from_docx"]
def extract_text_from_docx(file_path):
    """
    Extracts text from a .docx file with error handling.
    :param file_path: Path to the .docx file.
    :return: Extracted text as a string or an error message.
    """
    try:
        # Load the .docx file
        document = Document(file_path)
        
        # Initialize an empty string to store the extracted text
        extracted_text = ""

        # Iterate through each paragraph in the document
        for paragraph in document.paragraphs:
            extracted_text += paragraph.text + "\n"

        return extracted_text

    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except Exception as e:
        return f"Error extracting text from the .docx file: {e}"