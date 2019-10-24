import pandas as pd
import tweepy
import time
import datetime
from collections import deque


class TwitterMiner:

    def __init__(self, keys, keyword, last=500, once=1000):
        self.keys = keys
        self.keyword = keyword
        self.last_tweets = deque(maxlen=last)
        self.tweets_at_once = once
        auth = tweepy.OAuthHandler(self.keys['consumer_key'], self.keys['consumer_secret'])
        auth.set_access_token(self.keys['access_token_key'], self.keys['access_token_secret'])
        self.api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)
        print('Miner is ready!')

    def miner(self):
        data = []
        try:
            results = tweepy.Cursor(self.api.search, q=self.keyword, lang='en', tweet_mode='extended').items(
                self.tweets_at_once)
        except tweepy.TweepError:
            time.sleep(901)
            results = tweepy.Cursor(self.api.search, q=self.keyword, lang='en', tweet_mode='extended').items(
                self.tweets_at_once)

        for tweet in results:
            if tweet.id in self.last_tweets:
                continue
            self.last_tweets.append(tweet.id)
            hashtags = [tweet.entities["hashtags"][i]['text'] for i in range(0, len(tweet.entities["hashtags"]))]
            mined = {
                'tweet_id': tweet.id,
                'mined_at': str(datetime.datetime.now()),
                'name': tweet.user.name,
                'screen_name': tweet.user.screen_name,
                'followers_count': tweet.user.followers_count,
                'friends_count': tweet.user.friends_count,
                'user_location': tweet.user.location,
                'date': str(tweet.created_at),
                'text': tweet.full_text,
                'hashtags': hashtags,
                'retweet_count': tweet.retweet_count,
                'favorite_count': tweet.favorite_count,
                'device': tweet.source,
                'location': tweet.place
            }

            try:
                mined['retweet_text'] = tweet.retweeted_status.full_text
            except:
                mined['retweet_text'] = 'None'
            try:
                mined['quote_text'] = tweet.quoted_status.full_text
                mined['quote_screen_name'] = tweet.quoted_status.user.screen_name
            except:
                mined['quote_text'] = 'None'
                mined['quote_screen_name'] = 'None'
            try:
                mined['media'] = tweet.entities.media.media_url
            except:
                mined['media'] = 'None'
            try:
                mined['truncated_text'] = tweet.truncated
            except:
                mined['truncated_text'] = 'None'

            data.append(mined)

        return data

    def boss(self, wait=900, batch=96):
        while True:
            counter = 0
            twitter_data = {}
            while counter < batch:
                name = 'batch number ' + str(counter)
                print(name)
                twitter_data[name] = []
                twitter_data[name].append(self.miner())
                time.sleep(wait)
                counter += 1

            all_tweets = pd.concat([pd.DataFrame(twitter_data[i][0]) for i in twitter_data]).reset_index(drop=True)
            filename = 'tweets_about_' + self.keyword + '_' + str(datetime.date.today()) + '.csv'
            all_tweets.to_csv(filename)
