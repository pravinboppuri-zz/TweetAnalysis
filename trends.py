import os
import json
import tweepy
from tweepy import OAuthHandler
from google.cloud import bigquery
from env import upload_blob
client = bigquery.Client()


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/bella/key.json"


api_key = "kkk"
api_secret = "978978"
access_token = "187vj"
access_token_secret = "7897w"
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


INDIA_WOE_ID = 23424848
results = api.trends_place(INDIA_WOE_ID)

India_trends = api.trends_place(INDIA_WOE_ID)

trends = json.loads(json.dumps(India_trends, indent=1))

for trend in trends[0]["trends"]:
    value=json.dumps((trend["name"].strip("#")))
    #with open('/home/bella/PycharmProjects/TweetAnalysis/trend.csv','a') as f:
     #       f.write(value.strip('"'))
      #      f.write('\n')
       #     upload_blob('tweetanalysis',"trend.csv",'Input')
