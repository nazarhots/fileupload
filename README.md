# Flask File Upload Web Application
This is a simple Flask web application that allows users to upload files and download them back. The uploaded file is stored in the **'static/files'** folder. If a file with the same name already exists, it will be renamed with a unique ID to avoid overwriting.

## Prerequisites
Before running the application, make sure you have the following software installed on your machine:

- *Python (3.6 or higher)*
- *Flask (2.0.1 or higher)*


## Installation

1. Clone the repository:

```bash
git clone https://github.com/nazarhots/fileupload.git
```
2. Install the requirements:
```bash
pip install -r requirements.txt
```
3. Start the application by running the following command:
```bash   
 python3 app.py
 ```


 ## Usage
- Click the "Upload File" button to upload a file.

- The application will display information about the uploaded file, including its size, upload time, and upload speed.

- Click the "Download" button to download the uploaded file.