import os
import json
import tweepy
from tweepy import OAuthHandler
from google.cloud import bigquery
from env import upload_blob
client = bigquery.Client()


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/bella/key.json"


api_key = "05vmjOLTZazXj2doCsLYPXMgx"
api_secret = "OxV7iOFKA3x3nBBF9WHSpQ0w1SVcNdEjOt3GZPmFqDszahb31L"
access_token = "1427298992-FNne49AJM0fnq6ZiHBB7RcjcxsslFwLD7Uj4Pnj"
access_token_secret = "7V4RDqhgxaemcb42mbBIY50T6eSYDesN6TzMcrxZKohww"
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
