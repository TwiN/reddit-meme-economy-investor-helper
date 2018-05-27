from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import praw
import json
import os
import datetime


target_post = 'https://www.reddit.com/r/MemeEconomy/comments/8mhg5j/should_i_sell/'


# To create a client_id/client_secret, visit https://www.reddit.com/prefs/apps/
# Once you have a client_id & client_secret, just replace os.getenv('CLIENT_ID') by 'yourclientid'
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'),
                     client_secret=os.getenv('CLIENT_SECRET'),
                     user_agent='reddit-meme-economy-investor-helper')

scores = {}
app = Flask(__name__, static_url_path='/static/')


@app.route('/js/script.js')
def script():
    return app.send_static_file('js/script.js')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/scores')
def get_scores():
    return json.dumps(scores)


@app.route('/target')
def get_target():
    return json.dumps(target_post)


if __name__ == '__main__':
    app.run()


def fetch_submission_score():
    submission = reddit.submission(url=target_post)
    scores[datetime.datetime.now().strftime('%H:%M:%S')] = submission.score


# Fetch the score for the first time
fetch_submission_score()


# Automatically fetch the score every 5 seconds
scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(fetch_submission_score, 'interval', seconds=5)
scheduler.start()
