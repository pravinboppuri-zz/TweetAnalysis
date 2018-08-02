create view if not exists tweet.wordcount

AS select distinct word, sum(count) as count from 
(
SELECT word,count from `bigqueryproject-210006.123.wordcount_tweet`  
UNION all
SELECT word,count from `bigqueryproject-210006.123.wordcount_tweet1` 
UNION all
SELECT word,count from `bigqueryproject-210006.123.wordcount_tweet1` 
) xy

group by word
 
