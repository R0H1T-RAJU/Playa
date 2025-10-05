import emotions.emotionAnalyzer as eanalyzer
import speech.speechRec as sanalyzer
import tone.toneAnalyzer as tanalyzer
import os
import song.songmaker as songmaker
import song.songrequest as songrequest
import time


VIDEO_PATH = "videos/"
filename = "football.mov"

filepath = VIDEO_PATH + filename

emotions = eanalyzer.getEmotions(filepath)
speech = sanalyzer.getSpeechTranscript(filepath)
tone = tanalyzer.get_sentiment(speech)
os.remove("data.csv")
os.removedirs("output")

print(speech)
print(tone)
print(emotions)

# gemini ai prompt handler here

from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents='''I am going to give you a short conversation that someone said, the tone of which this person said it, and
                the emotions of the person's face of when they said it. I want you create a prompt that that should generate a song
                based off this. The prompt genre should be based off what they said. The inflection should match the tone. The emotions
                of the song should follow the emotions. ALSO IT IS IMPERATIVE WHAT U RETURN IS UNDER 270 characters.
                ''' + speech + tone + emotions
)

prompt = response.text
print("prompt: ", prompt)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents='''Use the song prompt that I am about to give you and generate song lyrics for a 30 second song about this prompt.
                ''' + prompt
)

lyrics = response.text
print("lyrics: ", lyrics)

song_task_id = songmaker.create_music_mp3(prompt, lyrics)
print(song_task_id)

download_url = None
time_interval = 15

while not download_url:
    download_url = songrequest.get_song_mp3(song_task_id)
    if not download_url:
        print(f"Conversion not ready yet. Retrying in {time_interval} seconds...")
        time.sleep(time_interval)

print("Download link:", download_url)