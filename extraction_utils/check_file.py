# try:
#     import magic
# except ImportError:
#     print("The 'magic' library is not installed. Install it using 'pip install python-magic' or 'pip install python-magic-bin' for Windows.")
#     raise

# __all__ =["check_file_type"]

# def check_file_type(file_path):
#     """
#     Checks the file type based on its MIME type with error handling.
#     :param file_path: Path to the file to be checked.
#     :return: File type ('pdf', 'docx', 'msword', or 'wrong_format') or an error message.
#     """
#     try:
#         # Initialize the magic object
#         mime = magic.Magic(mime=True)
#         file_type = mime.from_file(file_path)
        
#         # Check MIME type and return corresponding file type
#         if "application/pdf" in file_type:
#             return "pdf"
#         elif "application/vnd.openxmlformats-officedocument.wordprocessingml.document" in file_type:
#             return "docx"
#         elif "application/msword" in file_type:
#             return "msword"
#         else:
#             return "wrong_format"
#     except FileNotFoundError:
#         return f"Error: The file at {file_path} was not found."
#     except magic.MagicException as e:
#         return f"Error with the magic library: {e}"
#     except Exception as e:
#         return f"Error determining file type: {e}"


import mimetypes

__all__ = ["check_file_type"]

def check_file_type(file_path):
    """
    Checks the file type based on its MIME type using the `mimetypes` library.
    :param file_path: Path to the file to be checked.
    :return: File type ('pdf', 'docx', 'msword', or 'wrong_format') or an error message.
    """
    try:
        # Guess the MIME type based on the file extension
        mime_type, _ = mimetypes.guess_type(file_path)
        
        # Check MIME type and return corresponding file type
        if mime_type == "application/pdf":
            return "pdf"
        elif mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            return "docx"
        elif mime_type == "application/msword":
            return "msword"
        else:
            return "wrong_format"
    except Exception as e:
        return f"Error determining file type: {e}"
