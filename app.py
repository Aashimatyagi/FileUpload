from flask import Flask, request, jsonify, send_from_directory, render_template
import os
from werkzeug.utils import secure_filename
import datetime
from PIL import Image
import magic

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Utility functions

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_description(file_path):
    try:
        magic_obj = magic.Magic()
        file_type = magic_obj.from_file(file_path)
        return file_type
    except Exception as e:
        return str(e)

# Routes

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/files', methods=['GET'])
def get_files_info():
    return jsonify(uploaded_files)


@app.route('/get_image_metadata/<filename>', methods=['GET'])
def get_image_metadata(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image = Image.open(file_path)
        width, height = image.size
        format_name = image.format       
        exif_data = None
        if hasattr(image, '_getexif'):
            exif_data = image._getexif()

        return jsonify({
            'width': width,
            'height': height,
            'format': format_name,
            'exif_data': exif_data})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files')

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            file_description = get_file_description(file_path)

            file_info = {
                'filename': file.filename,
                'size': os.path.getsize(file_path),
                'url': f'/uploads/{filename}',
                'upload_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'description': file_description
            }

            uploaded_files.append(file_info)
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({'message': 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    uploaded_files = []
    app.run(host='0.0.0.0', port=5000)
