import pandas as pd
import numpy as np
from matplotlib import __version__
import matplotlib.pyplot as plt
import tweepy as tw
import json as json
import datetime as datetime
import time as time
# import textblob

print('Today is ' + str(datetime.date.today()))

print('Pandas version ' + pd.__version__)
print('Numpy version ' + np.__version__)
print('Matplotlib version ' + __version__)
print('Tweepy version ' + tw.__version__)
print('JSON package version ' + json.__version__)

# print('Check if the tokenizer is availble')
# example = textblob.TextBlob("Python is a high-level, general-purpose programming language.")
# try:
#     example.words
# except:
#     import nltk
#     nltk.download('punkt')