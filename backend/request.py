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
        

song_id = "ccbccb3e-e89b-45ed-bc8e-542640964492"
download_url = None
while not download_url:
    download_url = get_song_mp3(song_id)
    if not download_url:
        print("Conversion not ready yet. Retrying in 30 seconds...")
        time.sleep(30)

print("Download link:", download_url)
