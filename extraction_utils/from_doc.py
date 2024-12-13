import textract

__all__ = ["extract_text_from_doc"]
def extract_text_from_doc(file_path):
    """
    Extract text from a .doc file using textract.
    :param file_path: Path to the .doc file.
    :return: Extracted text as a string.
    """
    try:
        text = textract.process(file_path).decode("utf-8")
        return text
    except Exception as e:
        return f"Error extracting text from .doc file: {e}"