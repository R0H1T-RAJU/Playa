from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer
analyzer = SentimentIntensityAnalyzer()

def preprocess_text(text):

    tokens = word_tokenize(text.lower())

    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]


    lemmatizer = WordNetLemmatizer()

    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]


    processed_text = ' '.join(lemmatized_tokens)

    return processed_text


def get_sentiment(text):

    scores = analyzer.polarity_scores(text)

    return scores

def tone_analysis(text):

    processText = preprocess_text(text)

    print(get_sentiment(processText))