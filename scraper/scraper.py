#twitter twitter_iot_scraper
import concurrent.futures
import time
import os
import twitter

class scraper():
    def __init__(self):
        self.buildDir()

    def buildDir(self):
        if os.path.isdir('csv_results/'):
            os.mkdir('csv_results/')

    def getTweetsWithHashtag(self, hashtag):
        #get tweets with a hashtag specified as input
        tweets = []
        return tweets

    def writeTweetsToCSV(self, tweets):
        #write tweets to a csv
        return None


sc = scraper()
