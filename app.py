import os
import time
import uuid

from flask import Flask, render_template, request, send_from_directory, url_for


UPLOAD_FOLDER = 'static/files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    """Handles file uploads and returns the download.html template."""
    start = time.time()
    file = request.files['file']
    filename = file.filename
    
    if os.path.exists(os.path.join(UPLOAD_FOLDER, filename)):
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{uuid.uuid4().hex[:5]}{ext}"
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    execution_duration = time.time() - start
    file_size_b = os.path.getsize(os.path.join(UPLOAD_FOLDER, filename))
    upload_speed = file_size_b / (execution_duration * 1000000)
    file_size_mb = file_size_b / 1048576
    download_url = request.host_url + url_for('download', filename=filename)

    return render_template('download.html', duration=execution_duration, upload_speed=upload_speed, filename=filename,
                           download_url=download_url, file_size=file_size_mb)


@app.route('/download/<filename>')
def download(filename: str):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
