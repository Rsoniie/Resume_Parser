
from flask import Flask, request, jsonify, render_template
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os
import spacy
from PyPDF2 import PdfReader
from docx import Document
from io import BytesIO
import re 
from pymongo import MongoClient

# Load environment variables
load_dotenv()

app = Flask(__name__)
# app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')  # For session management

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

# Connect to MongoDB
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
try:
    client = MongoClient(MONGO_URI)
    db = client['Project_R']  # Database name
    collection = db['resumes']  # Collection name
    print("Connected to MongoDB successfully.")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    exit(1)  # Exit if unable to connect to the database

# Load the SpaCy NER model
try:
    nlp = spacy.load('nlp_ner_model')
    print("SpaCy NER model loaded successfully.")
except Exception as e:
    print(f"Failed to load SpaCy model: {e}")
    exit(1)  # Exit if the model cannot be loaded

# Global variable to store the last uploaded file
global_uploaded_file = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global global_uploaded_file  # Reference the global variable

    if 'file' not in request.files:
        print("No file part in the request.")
        return jsonify({"error": "No file part in the request."}), 400

    file = request.files['file']

    if file.filename == '':
        print("No file selected for uploading.")
        return jsonify({"error": "No file selected for uploading."}), 400

    if file and (file.filename.lower().endswith('.pdf') or file.filename.lower().endswith('.docx')):
        try:
            # Upload the file to Cloudinary
            print(f"Uploading file '{file.filename}' to Cloudinary...")
            upload_result = cloudinary.uploader.upload(file, resource_type='auto')
            file_url = upload_result.get('secure_url')

            if not file_url:
                print("Failed to retrieve file URL from Cloudinary.")
                return jsonify({"error": "Failed to retrieve file URL from Cloudinary."}), 500

            print(f"File uploaded to Cloudinary successfully. URL: {file_url}")

            # Reset file pointer and store in memory
            file.seek(0)
            global_uploaded_file = {
                "filename": file.filename,
                "content": BytesIO(file.read()),  # Store the file content
                "file_url": file_url
            }
            print("File stored in memory for processing.")
            return jsonify({
                "message": "File uploaded successfully.",
                "filename": file.filename,
                "file_url": file_url
            }), 200
        except Exception as e:
            print(f"File upload failed: {e}")
            return jsonify({"error": f"File upload failed: {str(e)}"}), 500
    else:
        print("Invalid file type uploaded.")
        return jsonify({
            "error": "Invalid file type. Only PDF and DOCX files are allowed."
        }), 400

@app.route('/extract_text', methods=['POST'])
def extract_text():
    global global_uploaded_file  # Reference the global variable

    if not global_uploaded_file:
        print("No file has been uploaded yet.")
        return jsonify({"error": "No file has been uploaded yet."}), 400

    try:
        filename = global_uploaded_file["filename"]
        content = global_uploaded_file["content"]
        file_url = global_uploaded_file["file_url"]
        content.seek(0)  # Reset the file pointer

        print(f"Starting text extraction for file '{filename}'.")

        text = ""
        entities_list = []

        if filename.lower().endswith('.pdf'):
            # Extract text from PDF
            print("Extracting text from PDF...")
            pdf_reader = PdfReader(content)
            for page_num, page in enumerate(pdf_reader.pages, start=1):
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + "\n"
                    print(f"Extracted text from page {page_num}.")
                else:
                    print(f"No text found on page {page_num} of the PDF.")
        
        elif filename.lower().endswith('.docx'):
            # Extract text from DOCX
            print("Extracting text from DOCX...")
            doc = Document(content)
            for para in doc.paragraphs:
                text += para.text + "\n"
            print("Text extraction from DOCX completed.")

        else:
            print("Unsupported file type for text extraction.")
            return jsonify({"error": "Unsupported file type for text extraction."}), 400
        
        # Clean the extracted text
        text = re.sub(r"\s+", " ", text).strip()
        print("Extracted text cleaned.")

        if not text:
            print("No text could be extracted from the file.")
            return jsonify({"error": "No text could be extracted from the file."}), 400

        # Process the text with the NER model
        print("Performing Named Entity Recognition (NER) on the extracted text...")
        doc = nlp(text)
        entities_list = [{"entity": ent.text, "label": ent.label_} for ent in doc.ents]
        print(f"NER completed. Found {len(entities_list)} entities.")

        # Insert the document into MongoDB
        print("Inserting document into MongoDB...")
        document_id = collection.insert_one({
            "filename": filename,
            "file_url": file_url,
            "entities": entities_list
        }).inserted_id
        print(f"Document inserted into MongoDB with ID: {document_id}")

        # Return extracted text and entities
        print("Text extraction and entity recognition were successful.")
        return jsonify({
            "message": "Text extraction and entity recognition were successful.",
            "text": text,
            "entities": entities_list,
            "document_id": str(document_id)
        }), 200

    except Exception as e:
        print(f"An error occurred during text extraction: {e}")
        return jsonify({"error": f"An error occurred during text extraction: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app
    print("Starting Flask application...")
    app.run(debug=True, port=3000)
