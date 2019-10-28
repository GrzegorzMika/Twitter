import scrappers
from pathlib import Path

twitter_keys = Path('../Twitter_API_key.txt').read_text().split('\n')
twitter_keys = {
    'consumer_key': twitter_keys[0],
    'consumer_secret': twitter_keys[1],
    'access_token_key': twitter_keys[2],
    'access_token_secret': twitter_keys[3]
}

TwitterMiner = scrappers.TwitterMiner(keys=twitter_keys, keyword='#brexit', last=1000, once=5000)
TwitterMiner.boss(batch=4)
