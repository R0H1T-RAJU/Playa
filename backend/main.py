import emotions.emotionAnalyzer as analyzer
import speech.speechRec as sr
import os

filename = "videos/video.mov"

emotions = analyzer.getEmotions(filename)
speech = sr.getSpeechTranscript(filename)

print(speech)
print(emotions)

os.remove("data.csv")
os.removedirs("output")