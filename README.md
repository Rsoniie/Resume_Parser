<!-- # <span style="color:blue;">Resume Parser</span>

This project is a Flask-based web application designed for parsing resumes in PDF or DOCX format. It extracts text, identifies named entities using an NER (Named Entity Recognition) model, and stores the parsed data in a MongoDB database. The application also integrates Cloudinary for file storage.

## <span style="color:green;">Features</span>

- Upload resumes in PDF or DOCX format.
- Extract text from uploaded files.
- Perform Named Entity Recognition (NER) using a pre-trained SpaCy model.
- Store extracted text and entities in a MongoDB database.
- Use Cloudinary for secure file storage.

## <span style="color:green;">Prerequisites</span>

Ensure the following are installed on your system:

- Python 3.7 or later
- Flask
- MongoDB
- Cloudinary account
- SpaCy and a custom NER model
- PyPDF2 and python-docx for text extraction

## <span style="color:green;">Setup and Installation</span>

1. **<span style="color:orange;">Clone the Repository</span>**

   ```bash
   git clone https://github.com/Rsoniie/Resume_Parser.git
   cd Resume_Parser
   ```

2. **<span style="color:orange;">Create and Activate a Virtual Environment</span>**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **<span style="color:orange;">Install Dependencies</span>**

   ```bash
   pip install -r requirements.txt
   ```

4. **<span style="color:orange;">Set Up Environment Variables</span>**

   Create a `.env` file in the project root and add the following configuration:

   ```env
   CLOUDINARY_CLOUD_NAME=your_cloud_name
   CLOUDINARY_API_KEY=your_api_key
   CLOUDINARY_API_SECRET=your_api_secret

   ```

   Replace placeholders with your actual Cloudinary and MongoDB credentials.

5. **<span style="color:orange;">Set Up the NER Model</span>**

   - Unzip the `nlp_ner_model.zip` file and place the extracted folder in the project directory.
   - Ensure the model is loaded correctly in `app.py`:
     ```python
     nlp = spacy.load('nlp_ner_model')
     ```

6. **<span style="color:orange;">Run the Application</span>**

   ```bash
   python app.py
   ```

   The application will run on `http://127.0.0.1:3000`.

## <span style="color:green;">Endpoints</span>

### 1. `/` (GET)

- Renders the homepage.

### 2. `/upload` (POST)

- Uploads a resume file.
- Accepted file types: PDF, DOCX.
- Returns:
  ```json
  {
    "message": "File uploaded successfully.",
    "filename": "example.pdf",
    "file_url": "https://cloudinary.com/..."
  }
  ```

### 3. `/extract_text` (POST)

- Extracts text and entities from the last uploaded file.
- Returns:
  ```json
  {
    "message": "Text extraction and entity recognition were successful.",
    "text": "Extracted text here...",
    "entities": [
      {"entity": "John Doe", "label": "PERSON"},
      {"entity": "Google", "label": "ORG"}
    ],
    "document_id": "mongodb_document_id"
  }
  ```

## <span style="color:green;">File Structure</span>

```
Resume_Parser/
├── .env
├── .gitignore
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── nlp_ner_model/
├── static/
│   └── css/
├── uploads/
```

## <span style="color:green;">Important Files</span>

- **app.py**: Main Flask application.
- **.env**: Environment variables for Cloudinary and MongoDB.
- **nlp\_ner\_model**: Directory containing the SpaCy NER model.
- **templates/index.html**: Frontend template.
- **static/**: Directory for static files (e.g., CSS, JavaScript).
- **uploads/**: Directory for storing uploaded files temporarily.

## <span style="color:green;">Troubleshooting</span>

1. **<span style="color:orange;">MongoDB Connection Issues</span>**:

   - Ensure the MongoDB server is running.
   - Verify the `MONGO_URI` in the `.env` file.

2. **<span style="color:orange;">Cloudinary Upload Failures</span>**:

   - Check the `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`, and `CLOUDINARY_CLOUD_NAME` in the `.env` file.

3. **<span style="color:orange;">NER Model Loading Errors</span>**:

   - Confirm the `nlp_ner_model` directory exists and contains the required files.

## <span style="color:green;">License</span>

This project is licensed under the MIT License. See the LICENSE file for details.

## <span style="color:green;">Author</span>

- Roshan Soni
 -->




# <span style="color:blue;">Resume Parser</span>

This project is a Flask-based web application designed for parsing resumes in PDF or DOCX format. It extracts text, identifies named entities using an NER (Named Entity Recognition) model, and stores the parsed data in a MongoDB database. The application also integrates Cloudinary for file storage.

## <span style="color:green;">Features</span>

- Upload resumes in PDF or DOCX format.
- Extract text from uploaded files.
- Perform Named Entity Recognition (NER) using a pre-trained SpaCy model.
- Store extracted text and entities in a MongoDB database.
- Use Cloudinary for secure file storage.
- Save extracted entities locally as JSON files.

## <span style="color:green;">Prerequisites</span>

Ensure the following are installed on your system:

- Python 3.7 or later
- Flask
- MongoDB
- Cloudinary account
- SpaCy and a custom NER model
- PyPDF2 and python-docx for text extraction

## <span style="color:green;">Setup and Installation</span>

1. **<span style="color:orange;">Clone the Repository</span>**

   ```bash
   git clone https://github.com/Rsoniie/Resume_Parser.git
   cd Resume_Parser
   ```

2. **<span style="color:orange;">Create and Activate a Virtual Environment</span>**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **<span style="color:orange;">Install Dependencies</span>**

   ```bash
   pip install -r requirements.txt
   ```

4. **<span style="color:orange;">Set Up Environment Variables</span>**

   Create a `.env` file in the project root and add the following configuration:

   ```env
   CLOUDINARY_CLOUD_NAME=your_cloud_name
   CLOUDINARY_API_KEY=your_api_key
   CLOUDINARY_API_SECRET=your_api_secret
   ```

   Replace placeholders with your actual Cloudinary and MongoDB credentials.

5. **<span style="color:orange;">Set Up the NER Model</span>**

   - Unzip the `nlp_ner_model.zip` file and place the extracted folder in the project directory.
   - Ensure the model is loaded correctly in `app.py`:
     ```python
     nlp = spacy.load('nlp_ner_model')
     ```

6. **<span style="color:orange;">Run the Application</span>**

   ```bash
   python app.py
   ```

   The application will run on `http://127.0.0.1:3000`.

## <span style="color:green;">Endpoints</span>

### 1. `/` (GET)

- Renders the homepage.

### 2. `/upload` (POST)

- Uploads a resume file.
- Accepted file types: PDF, DOCX.
- Returns:
  ```json
  {
    "message": "File uploaded successfully.",
    "filename": "example.pdf",
    "file_url": "https://cloudinary.com/..."
  }
  ```

### 3. `/extract_text` (POST)

- Extracts text and entities from the last uploaded file.
- Returns:
  ```json
  {
    "message": "Text extraction and entity recognition were successful.",
    "text": "Extracted text here...",
    "entities": [
      {"entity": "John Doe", "label": "PERSON"},
      {"entity": "Google", "label": "ORG"}
    ],
    "document_id": "mongodb_document_id"
  }
  ```

### 4. `/save` (POST)

- Saves the extracted global entities locally as a JSON file.
- Generates a unique filename with a timestamp for every save.
- Returns:
  ```json
  {
    "message": "Global entities saved locally as JSON successfully.",
    "output_file": "uploads/global_entities_20241214_153045.json",
    "entities": [
      {"entity": "John Doe", "label": "PERSON"},
      {"entity": "Google", "label": "ORG"}
    ]
  }
  ```

## <span style="color:green;">File Structure</span>

```
Resume_Parser/
├── .env
├── .gitignore
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── nlp_ner_model/
├── static/
│   └── css/
├── uploads/
```

## <span style="color:green;">Important Files</span>

- **app.py**: Main Flask application.
- **.env**: Environment variables for Cloudinary and MongoDB.
- **nlp\_ner\_model**: Directory containing the SpaCy NER model.
- **templates/index.html**: Frontend template.
- **static/**: Directory for static files (e.g., CSS, JavaScript).
- **uploads/**: Directory for storing uploaded files temporarily.

## <span style="color:green;">Troubleshooting</span>

1. **<span style="color:orange;">MongoDB Connection Issues</span>**:

   - Ensure the MongoDB server is running.
   - Verify the `MONGO_URI` in the `.env` file.

2. **<span style="color:orange;">Cloudinary Upload Failures</span>**:

   - Check the `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`, and `CLOUDINARY_CLOUD_NAME` in the `.env` file.

3. **<span style="color:orange;">NER Model Loading Errors</span>**:

   - Confirm the `nlp_ner_model` directory exists and contains the required files.

## <span style="color:green;">License</span>

This project is licensed under the MIT License. See the LICENSE file for details.

## <span style="color:green;">Author</span>

- Roshan Soni
