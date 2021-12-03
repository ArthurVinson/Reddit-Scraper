# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:03:22 2021

@author: Arthur Vinson

scrape takes a subreddit name as an argument and returns a dataframe

"""

import praw
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

reddit = praw.Reddit(
    client_id='LK_PUjO05BqFSg', 
    client_secret='FuE_G7UhRkvIsVNurMuo0VMO3J85ug', 
    user_agent='scraper project')

headlines = set()
for submission in reddit.subreddit('Reformed').new(limit=None):
    headlines.add(submission.title)
print(len(headlines))

df = pd.DataFrame(headlines)

# def subreddit_scrape(subreddit):
    