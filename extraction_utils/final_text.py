


from extraction_utils import check_file, from_doc, from_pdf, from_docs
__all__ = ["getting_final_text"]
def getting_final_text(file_path):
    my_file_type = check_file.check_file_type(file_path)

    if my_file_type == "pdf":
        text = from_pdf.extract_text_from_pdf(file_path)
        return text
    elif my_file_type == "docx":
        text = from_docs.extract_text_from_docx(file_path)
        return text
    elif my_file_type == "msword":
        text = from_doc.extract_text_from_doc(file_path)
        return text
    else :
        return "Use diff format (.pdf, .docx)"
