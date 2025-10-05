from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv("SONG_KEY")

API_URL = "https://api.musicgpt.example.com/v1/generate"  # replace with real MusicGPT endpoint

payload = {
    "prompt": "Calm ocean-themed background music with soft vocals",
    "lyrics": """Across the waves, so calm and blue,
                 The ocean whispers, calling you.
                 Gentle tides and skies above,
                 Carry peace, and endless love.""",
    "duration": 30,         # seconds
    "format": "mp4",        # or mp3/wav depending on API support
    "vocals": True,         # tell MusicGPT to include vocals
    "style": "ambient",     
    "mood": "calm"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

response = requests.post(API_URL, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Track generation started:", data)
    # You may get a task_id and need to poll a /status or /tasks endpoint
else:
    print("Error:", response.status_code, response.text)
