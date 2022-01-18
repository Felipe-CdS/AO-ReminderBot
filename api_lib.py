import tweepy
from decouple import config

def get_client():
    client = tweepy.Client(
    consumer_key= config('API_KEY'),
    consumer_secret= config('API_KEY_SECRET'),
    access_token= config('ACCESS_KEY'),
    access_token_secret= config('ACCESS_TOKEN_SECRET')
    )
    return client

def TEST_get_client():
    client = tweepy.Client(
    consumer_key= config('TEST_API_KEY'),
    consumer_secret= config('TEST_API_KEY_SECRET'),
    access_token= config('TEST_ACCESS_KEY'),
    access_token_secret= config('TEST_ACCESS_TOKEN_SECRET')
    )
    return client

def new_tweet(x):
    if(config('ENVIRONMENT') == 'LIVE'):        
        client = get_client()
    else:
        client = TEST_get_client()
    
    response = client.create_tweet( text=x )
    return response