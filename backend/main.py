import emotions.emotionAnalyzer as eanalyzer
import speech.speechRec as sanalyzer
import tone.toneAnalyzer as tanalyzer
import os
import song.songmaker as songmaker
import song.songrequest as songrequest
import time

VIDEO_PATH = "videos/"
filename = "random.mov"

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

prompt = "filler"
lyrics = "filler"

song_task_id = songmaker.create_music_mp3(prompt, lyrics)

download_url = None
while not download_url:
    download_url = songrequest.get_song_mp3(song_task_id)
    if not download_url:
        print("Conversion not ready yet. Retrying in 30 seconds...")
        time.sleep(30)

print("Download link:", download_url)