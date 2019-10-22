import tweepy as tw

twitter_keys = {
    'consumer_key':        'g3OU7SzfpnE2AoPzWzC7My8O9',
    'consumer_secret':     'kIOJAjk4Zun00BvCNCgK4NCSq2X5suMb88IJ12UcSzQUhVLiie',
    'access_token_key':    '953693483012902912-fXIsILeot5yu6LLk7BBxUiEfi4DwrQD',
    'access_token_secret': 'vNhUqPByb1SZQMIVuGwhJX8BaGAkROiEMVQ3N6JyYEB2l'
}

def authorization(keys):
    auth = tw.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token_key'], keys['access_token_secret'])
    api = tw.API(auth, wait_on_rate_limit_notify=True)
    return api

api = authorization(twitter_keys)

print(api)