import os
import json
from lib import *
# from flask import Flask, request, send_from_directory, make_response

# app = Flask(__name__)

# @app.route("/webhook", methods=["POST"])
def twitter_event_received(request):
    requestJson = request.get_json()
    # requestJson = json.load(open('testrequest.json', 'r'))
    # print(json.dumps(requestJson))

    # メンションツイートだった場合
    if 'tweet_create_events' in requestJson.keys() and 'user_has_blocked' in requestJson.keys():
        tweetObject = requestJson['tweet_create_events'][0]
        mention_text = tweetObject.get('text')
        print(mention_text)
        basedir = os.path.dirname(os.path.abspath(__file__))
        generate_video_from_mention_tweet(tweetObject, basedir)
    return ('', '200')

# twitter_event_received()
