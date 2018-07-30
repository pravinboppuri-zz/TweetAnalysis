
import json
from datetime import datetime
import string
import re


def get_time(tweet):
    return datetime.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")


def process_or_store(tweet):
    print(json.dumps(tweet,indent=1))