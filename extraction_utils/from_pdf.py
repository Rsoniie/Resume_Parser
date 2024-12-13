from PyPDF2 import PdfReader

__all__ = ["extract_text_from_pdf"]  # Explicitly declare exportable symbols

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file with error handling.
    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string or an error message.
    """
    try:
        # Create a PDF reader object
        reader = PdfReader(pdf_path)
        
        # Initialize an empty string to hold the extracted text
        extracted_text = ""

        # Iterate over all pages and extract text
        for page in reader.pages:
            extracted_text += page.extract_text()

        return extracted_text
    
    except FileNotFoundError:
        return f"Error: The file at {pdf_path} was not found."
    except Exception as e:
        return f"Error extracting text from the PDF: {e}"
