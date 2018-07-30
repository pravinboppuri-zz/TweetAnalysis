from __future__ import print_function
import json
import os
import tweepy
from tweepy import OAuthHandler
from env import upload_blob
from datetime import datetime
from json import dumps
from util import get_time
from trends import trends
import string
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/bella/key.json"


api_key = "05vmjOLTZazXj2doCsLYPXMgx"
api_secret = "OxV7iOFKA3x3nBBF9WHSpQ0w1SVcNdEjOt3GZPmFqDszahb31L"
access_token = "1427298992-FNne49AJM0fnq6ZiHBB7RcjcxsslFwLD7Uj4Pnj"
access_token_secret = "7V4RDqhgxaemcb42mbBIY50T6eSYDesN6TzMcrxZKohww"
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)


def get_tweets(text):

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        INDIA_WOE_ID = 23424848
        India_trends = api.trends_place(INDIA_WOE_ID)

        #value = process_or_store(India_trends)

        q = ('LunarEclipse')

        tt = tweepy.Cursor(api.search, q=q, lang='en').items(100)
        for tweet in tt:
            value=json.dumps(tweet.text)
            with open('/home/bella/PycharmProjects/TweetAnalysis/tweet.txt','a') as f:
                f.write(value.strip('"'))
                f.write('\n')
                upload_blob('tweetanalysis',"tweet.txt",'Input')



if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("twitter-handle")




