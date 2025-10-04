import emotions.emotionAnalyzer as eanalyzer
import speech.speechRec as sanalyzer
import tone.toneAnalyzer as tanalyzer
import os

VIDEO_PATH = "videos/"
filename = "random.mov"

filepath = VIDEO_PATH + filename

emotions = eanalyzer.getEmotions(filepath)
speech = sanalyzer.getSpeechTranscript(filepath)
tone = tanalyzer.get_sentiment(speech)

print(speech)
print(tone)
print(emotions)

os.remove("data.csv")
os.removedirs("output")