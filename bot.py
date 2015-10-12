import os
import time

import tweepy

class TwitterAPI:
    """
    Class for accessing the Twitter API.

    Requires API credentials to be available in environment
    variables. These will be set appropriately if the bot was created
    with init.sh included with the heroku-twitterbot-starter
    """
    def __init__(self):
        consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
        consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        """Send a tweet"""
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
<<<<<<< HEAD
    twitter.tweet("four tweets now...")
=======
    twitter.tweet("Hello world!") #You probably want to remove this line
>>>>>>> 3b04a84739a888c97370c818d254141fcdf2cbbe
    while True:
        #Send a tweet here!
        time.sleep(60)
