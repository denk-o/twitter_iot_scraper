#twitter twitter_iot_scraper
import concurrent.futures
from threading import Thread
from queue import Queue
import time
import os
import config
import twitter
import tweepy
import csv

class scraper():
    def __init__(self):
        self.buildDir()

        self.API_KEY = config.API_KEY
        self.SECRET = config.SECRET
        self.ACCESS_KEY = config.ACCESS_KEY
        self.ACCESS_SECRET = config.ACCESS_SECRET
        self.MAX_TWEETS = 2000

        self.tweets = []
        self.task_queue = Queue()

        auth = tweepy.OAuthHandler(self.API_KEY, self.SECRET)
        auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)

        self.api = tweepy.API(auth)
        # self.api = twitter.Api(consumer_key=self.API_KEY, consumer_secret=self.SECRET, access_token_key=self.ACCESS_KEY, access_token_secret=self.ACCESS_SECRET)

    def buildDir(self):
        if not os.path.isdir('csv_results/'):
            os.mkdir('csv_results/')
        if not os.path.isfile('csv_results/results.csv'):
            open('results.csv', 'w').close()

    def getTweetsWithIoT(self):
        counter = 0

        for tweet in tweepy.Cursor(self.api.search, q='#iot', count=100).items():
            # print(tweet.text)
            counter = counter + 1
            self.tweets.append(tweet)
            print(tweet.id)
            if counter == self.MAX_TWEETS:
                break
        # results = self.api.search(q='#iot', count=100)

        return self.tweets

    def getTweetsWithHashtag(self, hashtag):
        #get tweets with a hashtag specified as input
        tweets = []
        return tweets

    def writeTweetToCSV(self, tweet):
        #write tweets to a csv
        csvFile = open('results.csv', 'a')
        writer = csv.writer(csvFile)

        writer.writerow([tweet.text])
        writer.writerow('-')
        return None

    def worker(self):
        while True:
            next_tweet = self.task_queue.get()
            self.writeTweetToCSV(next_tweet)

            self.task_queue.task_done()
    def writeTweets(self):
        threads = [Thread(target=self.worker) for i in range(4)]

        [self.task_queue.put(tweet) for tweet in self.tweets]

        [thread.start() for thread in threads]

        self.task_queue.join()

sc = scraper()
sc.getTweetsWithIoT()
print('thread start')
sc.writeTweets()
print('task complete')
