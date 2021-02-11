# Reddit Scraper
# Arthur Vinson
# 2/8/2021

# This scraper will do the following:
# 1. Grab a collection of reddit comments from a selected subreddit using PRAW
# 2. Perform sentiment analysis. 

# Simple, no?

# --- Grabbing Comments from Reddit ---
# https://praw.readthedocs.io/en/latest/

import praw

# create a reddit instance and provide it with client_id, client_secreat and a user_agent
reddit = praw.Reddit(client_id='LK_PUjO05BqFSg', client_secret='FuE_G7UhRkvIsVNurMuo0VMO3J85ug', user_agent='scraper project')



# future project will scrape (all of?) reddit for a keyword or key phrase and conduct sentiment analysis on comments it finds