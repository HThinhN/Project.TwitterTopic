from settings import *
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle


class Sentiment_Analysis:
    def __init__(self):
        # Load dataset from TweetEval
        self.dataset = load_dataset(TWEET_DATASET, SENTIMENT_TYPE)

        # Get data and label 
        self.tweets = self.dataset['train']['text']
        self.labels = self.dataset['train']['label']

        # Split train data and test data 
        self.X_train, self.X_test, self.y_train, self.y_test = \
        train_test_split(self.tweets, self.labels, test_size=0.2, random_state=42)

        # Init TfidfVectorizer
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.X_train_tfidf = self.vectorizer.fit_transform(self.X_train)

        # Build model Logistic Regression
        self.model = LogisticRegression(max_iter=1000)

    def preprocessing(self, raw_data = None):
        data = self.vectorizer.transform(raw_data)

        return data
    
    def train_model(self):
        self.model.fit(self.X_train_tfidf, self.y_train)
    
    def save_model(self, model_name):
        with open(model_name, 'wb') as file:
            pickle.dump(self.model, file)

    def run(self, raw_data = None):
        # Using model to predict
        if not raw_data: 
            raw_data = self.X_test

        data = self.preprocessing(raw_data)
        y_pred  = self.model.predict(data)

        # Mapping result to label {negative, neutral, positive}
        label_mapping = {0: 'negative', 1: 'neutral', 2: 'positive'}
        predicted_class = label_mapping[y_pred[0]]

        if raw_data != self.X_test: 
            print(f"Text: {raw_data[0]}")
            print(f"Predicted Sentiment: {predicted_class}")
        else:
            print(classification_report(self.y_test, y_pred, target_names=['negative', 'neutral', 'positive']))


# sa = Sentiment_Analysis()
# raw_data = ["I hate using this product, it's so bad!"]
# sa.run(raw_data)