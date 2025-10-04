import warnings
warnings.filterwarnings('ignore')

from fer import FER
from fer import Video
import emotions.emotionAverager as ea

def getEmotions(filename):
    video = Video(filename)
    detector = FER(mtcnn=True)

    raw_data = video.analyze(detector, display=False, save_frames=False, save_video=False,)
    df = video.to_pandas(raw_data)

    return ea.average_emotions(df)


