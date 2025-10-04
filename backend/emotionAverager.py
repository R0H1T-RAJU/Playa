import pandas as pd

def average_emotions(df):

    # Correct emotion column names from FER
    emotions = ["angry","disgust","fear","happy","neutral","sad","surprise"]

    # Function to get dominant emotion for a row
    def get_dominant_emotion(row):
        emotion_probs = row[emotions]
        max_idx = emotion_probs.idxmax()
        return max_idx

    # Add a dominant emotion column
    df['dominant_emotion'] = df.apply(get_dominant_emotion, axis=1)

    # Group by consecutive dominant emotions
    timeline = []
    if not df.empty:
        start_idx = 0
        current_emotion = df.loc[0, 'dominant_emotion']

        for i in range(1, len(df)):
            if df.loc[i, 'dominant_emotion'] != current_emotion:
                # Save current segment
                timeline.append({
                    'emotion': current_emotion,
                    'start_frame': start_idx,
                    'end_frame': i-1
                })
                # Update for new segment
                start_idx = i
                current_emotion = df.loc[i, 'dominant_emotion']

        # Add the last segment
        timeline.append({
            'emotion': current_emotion,
            'start_frame': start_idx,
            'end_frame': len(df)-1
        })

    # Build timeline string
    x = ""
    for segment in timeline:
        x += f"{segment['emotion']} from frame {segment['start_frame']} to {segment['end_frame']}\n"
    return x
