from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv("SONG_KEY")

API_URL = "https://api.musicgpt.com/api/public/v1/MusicAI"  # replace with real MusicGPT endpoint

payload = {
    "prompt": "Trap rap song about what i had for breakfast",
    "lyrics": """Woke up, ice cold chain, skillet on flame,
                Eggs sunny side, money on my brain,
                Pour the syrup, drip like it’s rain,
                Toast on the plate, I don’t do plain.

                Sippin’ on orange juice, pockets full of juice,
                Bacon crispy, grind never loose,
                Stackin’ pancakes, syrup like a noose,
                Breakfast boss, yeah, I cuttin’ no truce.

                Cereal poppin’, countin’ up the knots,
                Pour the milk heavy, drip drip like the guap,
                Breakfast club flex, yeah, we settin’ the plots,
                Every bite rich, every bite hits the spot.""",
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
