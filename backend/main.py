import emotions.emotionAnalyzer as analyzer
import speech.speechRec as sr
import os

VIDEO_PATH = "videos/"
filename = "random.mov"

filepath = VIDEO_PATH + filename

emotions = analyzer.getEmotions(filepath)
speech = sr.getSpeechTranscript(filepath)

print(speech)
print(emotions)

os.remove("data.csv")
os.removedirs("output")