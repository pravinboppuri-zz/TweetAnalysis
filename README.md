# twitter-analysis-bigquery

As part of this analysis I've built an ETL using Apache Beam :-python (Google Dataflow) to get data from twitter on what people say about trending topics in India. Services used in google cloud are Dataflow , cloud storage, Bigquerybig




## twitter.py

This peice of code calls the twitter API and retunrs me the 'TEXT' of trending topic of my choice ="lunareclipse" and writes it into cloud datastore. I can also make use of Steaming API but for this use case i prefer to do analysis per one trending topic to do a word count analysis.

## trends.py

I capture all the trending topics in India with the Twitter search API 

## wordcount_test

This is my main class where I am making use of Google Dataflow pipeline with Apache Beam framework for my data processing. Cloud storage is used for storing the output

## bigquery_load.py

To make use of Googles Enterprise Datawarehouse, the above code manages to load my output into bigquery tables via google client. I 

## env.py

This is basically to store all the environment variables to connect to google cloud

## util.py

All methods are created in my utility to perform different transformations in the logic

## Improvements

1) End to End pipeline to perform twitter anlysis and word count can be automated
2) MAchine learning algorithms can be implemented to bring out words related to a particular trend
3) Streaming API can be used to capture live tweets with the help of google pub/sub events

