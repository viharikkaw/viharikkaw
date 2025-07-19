#pip install tweepy 
import tweepy
from transformers import pipeline 
api_key="vsFAyHTwTeagNJkcmfFSakVTkT"
api_key_secrete="zLZsRavhJabZgEptXO7mNvX6NbsnJ0G9LiopEJfMlQ0SQDtJMf"
access_token="1942591240954077186-K3Zl5UpDGRDMKD0jFmrFUULD6YnlGD"
access_token_secret="SphwVAxNXLgTNJ7rI75V8v27iRftDD7s2plU03OfTHWd5"
auth=tweepy.OAuth1UserHandler(api_key,api_key_secrete,access_token,access_token_secret)
api=tweepy.API(auth) 
sentimental_analyzer=pipeline("sentiment-analysis") 
api.search_tweets(q="#INDvsENG",lang="eng",count=10)