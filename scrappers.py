class TwitterMiner:

    def __init__(self, keys):
        self.keys = keys
        auth = tweepy.OAuthHandler(self.keys['consumer_key'], self.keys['consumer_secret'])
        auth.set_access_token(self.keys['access_token_key'], self.keys['access_token_secret'])
        self.api = tweepy.API(auth, wait_on_rate_limit_notify=True)
