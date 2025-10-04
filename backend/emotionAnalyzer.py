import warnings
warnings.filterwarnings('ignore')

from fer import FER
import pprint
from fer import Video
import cv2



img = cv2.imread("tanay.png")

video_filename = "expressions.mov"
video = Video(video_filename)

detector = FER()


raw_data = video.analyze(detector, display=True)
df = video.to_pandas(raw_data)

import emotionAverager as ea

timeline_str = ea.average_emotions(df)
print(timeline_str)
