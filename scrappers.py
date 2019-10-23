class TwitterMiner:

    def __init__(self, keys, last=500, once=1000):
        self.keys = keys
        self.last_tweets = last
        self.tweets_at_once = once
        auth = tweepy.OAuthHandler(self.keys['consumer_key'], self.keys['consumer_secret'])
        auth.set_access_token(self.keys['access_token_key'], self.keys['access_token_secret'])
        self.api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

    def miner(self, keyword):
        data = []
        try:
            results = tweepy.Cursor(self.api.search, q=keyword, lang='en', tweet_mode='extended').items(
                self.tweets_at_once)
        except tweepy.TweepError as e:
            time.sleep(901)
            results = tweepy.Cursor(self.api.search, q=keyword, lang='en', tweet_mode='extended').items(
                self.tweets_at_once)

        for tweet in results:
            # //TODO: look into Python Cookbook to compare with last tweets_at_once for uniqueness if tweet.id in :
            # continue
            mined = {
                'tweet_id': tweet.id,
                'mined_at': datetime.datetime.now(),
                'name': tweet.user.name,
                'screen_name': tweet.user.screen_name,
                'followers_count': tweet.user.followers_count,
                'friends_count': tweet.user.friends_count,
                'user_location': tweet.user.location,
                'data': tweet.created_at,
                'text': tweet.full_text,
                'hashtags': tweet.entities.hashtags,
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
