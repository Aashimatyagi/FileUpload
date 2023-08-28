# File Metadata Flask App

Welcome to the File Metadata Flask App documentation! This Flask-based application extracts and presents metadata from various file types, offering users insights into file details such as size, type, and upload date.

## Overview

The File Metadata Flask App allows users to:

- Upload diverse file formats, including images (JPEG, PNG, GIF), PDFs, and common document formats.
- Access file information like filename, size, URL, upload date, and description.

Built with Python and the Flask web framework, the application boasts an intuitive HTML frontend to ensure a user-friendly experience.

## Features

1. **File Upload**: Users can upload files through the web interface. Supported file formats include:
   - txt, pdf, png, jpg, jpeg, gif
   - csv, xlsx, docx

2. **File Details**: The app stores and displays essential information about uploaded files:
   - Filename
   - Size
   - URL
   - Upload date
   - Description

## API Definition

The app features two main endpoints:

- **`GET /`**: Renders the main page of the app, allowing users to upload files.

- **`POST /upload`**: Handles file uploads. Users can submit files via a form, and the server returns metadata about the uploaded file.

## RESTful Compliance

While the app follows RESTful principles by using HTTP methods (GET and POST), employing descriptive endpoint names, and utilizing JSON responses, it doesn't fully embrace REST architecture. Considerations for improvement include a refined resource-based structure and enhanced error-handling practices.

## HTTP Methods

- **GET**: Used for the homepage (`/`), rendering the HTML template for file uploads.

- **POST**: Used for file uploads (`/upload`). Users submit files via a form, and the server responds with metadata.

## API Endpoints

1. **`GET /`**: Renders the main page of the app, allowing users to upload files.

2. **Upload Endpoint**
    - **URL:** `/upload`
    - **Method:** `POST`
    - **Description:** Allows users to upload files for metadata extraction. Users submit a form with a "file" input field.
    - **Response:** JSON response containing metadata about the uploaded file. Errors result in appropriate error messages.

## Conclusion

The **File Upload App** provides an intuitive interface for uploading files and obtaining valuable metadata. The app's API endpoints adhere to REST principles, ensuring efficient interaction with its features. Users can seamlessly manage and explore their uploaded files using this application.
