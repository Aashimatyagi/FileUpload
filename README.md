File Metadata Flask App Documentation

This documentation provides an overview of the Flask app that extracts and displays metadata from various file types. The app allows users to upload files, and it returns information about the uploaded file's size, type, and upload date. The app supports multiple file formats, including images (JPEG, PNG, GIF), PDFs, and other common document formats.

The app is built using Python with the Flask web framework and includes both the server-side code and a simple HTML frontend for user interaction.

1. **File Upload**: Users can upload files through the web interface. The allowed file types include txt, pdf, png, jpg, jpeg, gif, csv, xlsx, and docx.

2. **File Information**: The app maintains information about uploaded files, including filename, size, URL, upload date, and a brief description.

API Definition

The app provides two main endpoints:

GET /: This endpoint renders the HTML template named index.html. It presents a user interface that allows users to upload files.

POST /upload: This endpoint handles file uploads. Users can upload a file using a form submission. The server processes the uploaded file and returns its metadata.

Clarity of REST

The app follows RESTful principles to a certain extent:

The app uses HTTP methods (GET and POST) to define different actions (rendering the upload form and handling file uploads).

The endpoints are named descriptively: / for the homepage and /upload for handling file uploads.

The app uses JSON responses to return metadata, making it easier for other applications to consume the data.

However, the app doesn't fully embrace REST principles:

It lacks a clear resource-based structure. While it does handle file uploads and metadata extraction, it's not a classic resource-oriented API.

It could benefit from better error handling and status code usage. The status codes returned in case of errors (e.g., 400 Bad Request) are appropriate, but there could be more detailed error messages.

Use of GET vs. POST

The app uses both GET and POST HTTP methods:

GET is used for the homepage (/). It renders the HTML template for the user interface where users can upload files.

POST is used for file uploads (/upload). Users submit a file through a form, and the server responds with the extracted metadata.

### API Endpoints

1. **`GET /`**: Renders the main page of the app, which allows users to upload files.


2.pload Endpoint

- **URL:** `/upload`
- **Method:** `POST`
- **Description:** This endpoint allows users to upload files for which they want to extract metadata. The server will process the uploaded file and return metadata about it.
- **Request Body:** The user should submit a form with a file input field named "file" to upload a file.
- **Response:** The server responds with JSON containing metadata about the uploaded file, including filename, size, description, and upload date. If the upload fails due to an invalid file type or other issues, an appropriate error message will be returned.

### Conclusion

The **File Upload App** provides a user-friendly interface for uploading various types of files and offers valuable information about uploaded files. The API endpoints follow REST principles to enable efficient interaction with the app's functionalities. Users can utilize the app to manage and explore their uploaded files with ease.
