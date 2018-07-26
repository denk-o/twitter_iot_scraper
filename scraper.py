#twitter twitter_iot_scraper
import concurrent.futures
from threading import Thread
from queue import Queue
import time
import os
import config
import twitter
import tweepy

class scraper():
    def __init__(self):
        self.buildDir()

        self.API_KEY = config.API_KEY
        self.SECRET = config.SECRET
        self.ACCESS_KEY = config.ACCESS_KEY
        self.ACCESS_SECRET = config.ACCESS_SECRET
        self.MAX_TWEETS = 2000

        auth = tweepy.OAuthHandler(self.API_KEY, self.SECRET)
        auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)

        self.api = tweepy.API(auth)
        # self.api = twitter.Api(consumer_key=self.API_KEY, consumer_secret=self.SECRET, access_token_key=self.ACCESS_KEY, access_token_secret=self.ACCESS_SECRET)

    def buildDir(self):
        if os.path.isdir('csv_results/'):
            os.mkdir('csv_results/')

    def getTweetsWithIoT(self):
        tweets = []
        count = 0

        for tweet in tweepy.Cursor(self.api.search, q='#iot', count=100).items():
            # print(tweet.text)
            count = count + 1
            tweets.append(tweet)
            print(tweet.id)
            if count == self.MAX_TWEETS:
                break
        # results = self.api.search(q='#iot', count=100)

        return tweets

    def getTweetsWithHashtag(self, hashtag):
        #get tweets with a hashtag specified as input
        tweets = []
        return tweets

    def writeTweetsToCSV(self, tweets):
        #write tweets to a csv
        return None


sc = scraper()
sc.getTweetsWithIoT()
