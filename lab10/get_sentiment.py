from flask import Flask, render_template, request, redirect, url_for
from joblib import load
import pandas as pd

pd.set_option('display.max_colwidth', 1000)

# Pre-loaded example tweets
EXAMPLE_TWEETS = [
    {
        'id': 1,
        'text': 'it\'s unbelievable that in the 21st century we\'d need something like this. again. #neverump  #xenophobia'
    },
    {
        'id': 2,
        'text': 'product of the day: happy man #wine tool  who\'s   it\'s the #weekend? time to open up &amp; drink up!'
    },
    {
        'id': 3,
        'text': '@user i\'m not interested in a #linguistics that doesn\'t address #race &amp; . racism is about #power. #raciolinguistics brings'
    },
    {
        'id': 4,
        'text': '@user why not @user mocked obama for being black.  @user @user @user @user #brexit'
    },
    {
        'id': 5,
        'text': 'yeah! new buttons in the mail for me they are so pretty! :) #jewelrymaking #buttons'
    }
]

class Tweet:
    def __init__(self, created_at, id, text):
        self.created_at = created_at
        self.id = id
        self.text = text


def get_related_tweets(text_query):
    tweets_list = []
    for tweet in [Tweet('2021', 1, text_query)]:  # Modified to use input text
        tweets_list.append({
            'created_at': tweet.created_at,
            'tweet_id': tweet.id,
            'tweet_text': tweet.text
        })
    return pd.DataFrame.from_dict(tweets_list)


pipeline = load("text_classification.joblib")


def requestResults(text):
    tweets = get_related_tweets(text)
    tweets['prediction'] = pipeline.predict(tweets['tweet_text'])
    prediction = "Positive" if tweets['prediction'].iloc[0] == 0 else "Negative"
    return {
        'text': text,
        'prediction': prediction
    }


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', examples=EXAMPLE_TWEETS)


@app.route('/', methods=['POST'])
def get_data():
    if request.method == 'POST':
        # Check if using example or manual input
        if 'example_select' in request.form and request.form['example_select'] != 'manual':
            text = request.form['example_select']
        else:
            text = request.form['search']
        
        results = requestResults(text)
        return render_template('home.html', results=results, examples=EXAMPLE_TWEETS)


if __name__ == '__main__':
    app.run(debug=True)