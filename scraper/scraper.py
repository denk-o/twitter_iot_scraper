#twitter twitter_iot_scraper
import concurrent.futures
import time
import os

class scraper():
    def __init__(self):
        self.buildDir()

    def buildDir(self):
        if os.path.isdir('csv_results/'):
            os.mkdir('csv_results/')

    def getTweetsWithHashtag(self, hashtag):
        #get tweets with a hashtag specified as input

    def writeTweetsToCSV(self):
        #write tweets to a csv
