#view script

create view if not exists tweet.toptrending

as select * from `tweet.wordcount` where LENGTH(word)>=5 
and word like '%eclip%' or word like '%lunar%' or word like '%moon%' or word like '%sun%' or word like '%planet%' or word like '%shine%' or word like '%beautiful%'
order by count desc
