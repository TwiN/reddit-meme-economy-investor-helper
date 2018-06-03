from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
import praw
import json
import os
import datetime


target_post: str = 'https://www.reddit.com/r/MemeEconomy/comments/8ock6k/acquire_everything/'


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


@app.route('/target', methods=['GET'])
def get_target():
    return json.dumps(target_post)


@app.route('/target', methods=['PUT'])
def update_target():
    global target_post
    target_post = request.get_json()['url']
    scores.clear()
    return json.dumps({'ERROR': False, 'MESSAGE': 'changed target_post to ' + target_post})


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
