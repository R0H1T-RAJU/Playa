from dotenv import load_dotenv
import requests
import os

load_dotenv()
api_key = os.getenv("SONG_KEY")
API_URL = "https://api.musicgpt.com/api/public/v1/MusicAI"  # replace with real MusicGPT endpoint

def create_music_mp3(prompt, lyrics):
    payload = {
        "prompt": prompt,
        "lyrics": lyrics,
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
        return data['conversion_id_1']
        # You may get a task_id and need to poll a /status or /tasks endpoint
    else:
        print("Error:", response.status_code, response.text)
