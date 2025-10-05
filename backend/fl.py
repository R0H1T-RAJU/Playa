from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from typing import Optional
import os
import uuid
import base64
import main

app = Flask(__name__)
UPLOAD_FOLDER = 'videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    return response


@app.route('/upload/', methods=['POST', 'OPTIONS'])
def upload_file():
    print(request)
    # "file" matches the key you appended in JS: formData.append('file', videoFile, videoFile.name)
    uploaded_file = request.files.get("file")

    if not uploaded_file:
        return {"error": "No file uploaded"}, 400

    # Save it with the original filename, or force .mov if you want
    filename = uploaded_file.filename or "output.mov"
    save_path = f"./videos/{filename}"

    uploaded_file.save(save_path)
    song_link = main.get_song_link(filename)

    return jsonify({"song_link": song_link})





def generate_filename_from_mimetype(mimetype: Optional[str]) -> str:
    extension_map = {
        'video/quicktime': '.mov',
        'video/webm': '.webm',
        'video/mp4': '.mp4',
    }

    normalized_mimetype = (mimetype or '').split(';')[0]
    extension = extension_map.get(normalized_mimetype, '.bin')
    return f"recording_{uuid.uuid4().hex}{extension}"

@app.route('/video_link/', methods=['POST'])
def getVideoStatus():
    return "not done"

if __name__ == '__main__':
    app.run(debug=True)
