import requests
from dotenv import load_dotenv
import time
import os

load_dotenv()

api_key = os.getenv("SONG_KEY")

def get_song_mp3(song_id):
    url = f"https://api.musicgpt.com/api/public/v1/byId?conversion_id={song_id}&conversionType=MUSIC_AI"
    headers = {
        "Authorization": api_key
    }

    response = requests.get(url, headers=headers)

    # check status
    if response.status_code == 200:
        data = response.json()  # if it's JSON
        return (data['conversion']['conversion_path_1'])
    else:
        print(f"Error {response.status_code}: {response.text}")
        


