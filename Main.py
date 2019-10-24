import scrappers

twitter_keys = {
    'consumer_key': 'g3OU7SzfpnE2AoPzWzC7My8O9',
    'consumer_secret': 'kIOJAjk4Zun00BvCNCgK4NCSq2X5suMb88IJ12UcSzQUhVLiie',
    'access_token_key': '953693483012902912-fXIsILeot5yu6LLk7BBxUiEfi4DwrQD',
    'access_token_secret': 'vNhUqPByb1SZQMIVuGwhJX8BaGAkROiEMVQ3N6JyYEB2l'
}

TwitterMiner = scrappers.TwitterMiner(keys=twitter_keys, keyword='#brexit')
TwitterMiner.boss()
