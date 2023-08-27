## File Upload App Documentation

This document provides an overview of the functionalities and usage of the **File Upload App**. The app is built using Flask and provides a web interface for users to upload various file types. The app also provides metadata and information about uploaded files. The API endpoints are designed following REST principles.

### Features

1. **File Upload**: Users can upload files through the web interface. The allowed file types include txt, pdf, png, jpg, jpeg, gif, csv, xlsx, and docx.

2. **File Metadata**: The app provides metadata about image files. It offers details such as image dimensions, format, and EXIF data if available.

3. **File Information**: The app maintains information about uploaded files, including filename, size, URL, upload date, and a brief description.

### API Endpoints

1. **`GET /`**: Renders the main page of the app, which allows users to upload files.

2. **`GET /files`**: Retrieves information about uploaded files.
   
   Response Format:
   ```json
   [
       {
           "filename": "example.png",
           "size": 1024,
           "url": "/uploads/example.png",
           "upload_date": "2023-08-28 15:30:00",
           "description": "PNG image"
       },
       // ...
   ]
   ```

3. **`GET /get_image_metadata/<filename>`**: Retrieves metadata for an image file with the given filename.

   Response Format:
   ```json
   {
       "width": 800,
       "height": 600,
       "format": "JPEG",
       "exif_data": {
           // EXIF data details
       }
   }
   ```

4. **`POST /upload`**: Uploads files through a form submission. The form field name is "files".

   Request:
   - Method: POST
   - Form Data: File(s) to be uploaded

   Response Format (Success):
   ```json
   {
       "message": "Files successfully uploaded"
   }
   ```

   Response Format (Error):
   ```json
   {
       "file1.txt": "File type is not allowed",
       "file2.docx": "File type is not allowed",
       // ...
   }
   ```

5. **`GET /uploads/<filename>`**: Retrieves a specific uploaded file by its filename.

### Usage

1. Start the Flask app by running `python app.py`.

2. Access the app in your web browser by navigating to `http://localhost:5000`.

3. On the main page, you can upload files using the provided form.

4. The app will display information about uploaded files, including name, size, URL, upload date, and description.

5. You can also access individual file metadata by clicking on the filename.

### Choosing Between GET and POST

In the context of RESTful API design:

- **GET** requests are used for retrieving data from the server. In this app, the `GET /files` endpoint retrieves information about uploaded files, and the `GET /get_image_metadata/<filename>` endpoint retrieves metadata for a specific image.

- **POST** requests are used for sending data to the server to create or update a resource. In this app, the `POST /upload` endpoint is used to upload files to the server.

### Conclusion

The **File Upload App** provides a user-friendly interface for uploading various types of files and offers valuable information about uploaded files. The API endpoints follow REST principles to enable efficient interaction with the app's functionalities. Users can utilize the app to manage and explore their uploaded files with ease.
