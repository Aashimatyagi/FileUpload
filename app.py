from flask import Flask, request, render_template, jsonify, send_file
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from PIL import Image
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(
    ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx', 'docx'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error='No file part'), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify(error='No selected file'), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        metadata = extract_metadata(filepath)
        os.remove(filepath)

        return jsonify(metadata)

    return jsonify(error='File upload failed. Invalid file type or extension.'), 400


def extract_metadata(filepath):
    metadata = {}

    if filepath.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        try:
            image = Image.open(filepath)
            image_metadata = image._getexif()
            metadata['file_type'] = 'Image'
            metadata['image'] = image_metadata
        except:
            pass

    if filepath.lower().endswith('.pdf'):
        try:
            pdf = PdfReader(filepath)
            metadata['file_type'] = 'PDF'
            metadata['pdf'] = {
                'num_pages': len(pdf.pages),
                'info': pdf.info
            }
        except:
            pass

    # Additional information
    filename = os.path.basename(filepath)
    file_extension = filename.rsplit('.', 1)[-1].lower()
    file_type = metadata.get('file_type', 'Unknown File Type')
    metadata['filename'] = filename
    metadata['size'] = os.path.getsize(filepath)
    # metadata['url'] = f'/download/{filename}'
    metadata['description'] = f'{file_type}/{file_extension}'
    metadata['upload_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return metadata


if __name__ == '__main__':
    app.run(debug=True)
