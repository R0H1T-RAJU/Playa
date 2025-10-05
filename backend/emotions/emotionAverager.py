import pandas as pd

def average_emotions(df, min_percentage=15):
    emotions = ["angry","disgust","fear","happy","neutral","sad","surprise"]

    # Function to get dominant emotion for a row
    def get_dominant_emotion(row):
        emotion_probs = row[emotions]
        return emotion_probs.idxmax()

    # Add dominant emotion column
    df['dominant_emotion'] = df.apply(get_dominant_emotion, axis=1)

    timeline = []
    if not df.empty:
        start_idx = 0
        current_emotion = df.loc[0, 'dominant_emotion']

        for i in range(1, len(df)):
            if df.loc[i, 'dominant_emotion'] != current_emotion:
                end_idx = i - 1
                seg_length = end_idx - start_idx + 1
                pct = (seg_length / len(df)) * 100

                if pct >= min_percentage:
                    timeline.append({
                        'emotion': current_emotion,
                        'start_frame': start_idx,
                        'end_frame': end_idx,
                        'percentage': pct
                    })

                start_idx = i
                current_emotion = df.loc[i, 'dominant_emotion']

        # Handle last segment
        end_idx = len(df) - 1
        seg_length = end_idx - start_idx + 1
        pct = (seg_length / len(df)) * 100

        if pct >= min_percentage:
            timeline.append({
                'emotion': current_emotion,
                'start_frame': start_idx,
                'end_frame': end_idx,
                'percentage': pct
            })

    # Build timeline string
    x = ""
    for segment in timeline:
        x += (
            f"{segment['emotion']} from frame {segment['start_frame']} "
            f"to {segment['end_frame']} ({segment['percentage']:.1f}%)\n"
        )

    return x
