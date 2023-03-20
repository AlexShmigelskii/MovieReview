import joblib
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def predict_review_sentiment(text):
    # cleaning text
    tokens = word_tokenize(text)
    filtered_review = " ".join([lemmatizer.lemmatize(word.lower()) for word in tokens
                                if not word.lower() in stop_words
                                and word.isalpha()])

    if len(filtered_review) != 0:

        # vectorizing text
        X = vectorizer.transform([filtered_review])

        # making prediction
        y_new = sentiment_model.predict(X)
        r_new = rating_model.predict(X)

        sentiment = "negative" if y_new == 0 else "positive"
        rating = int(r_new)

        return sentiment, rating

    else:
        sentiment = 'neutral'
        rating = 0

        return sentiment, rating




# loading model and vectorizer
sentiment_model = joblib.load('reviews/models/reg_sentiment_model14.joblib')
rating_model = joblib.load('reviews/models/reg_rating_model14.joblib')
vectorizer = joblib.load('reviews/models/vectorizer14.pkl')


