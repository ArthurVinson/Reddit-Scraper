# Reddit Scraper
# Arthur Vinson
# 2/8/2021

# This scraper will do the following:
# 1. Grab a collection of reddit comments from a selected subreddit using PRAW
# 2. Perform sentiment analysis. 

# Simple, no?

# Your task is to split posts into sentences, tag them with a PoS tagger that we will provide, gather some
# feature information from each post, learn models, and use these to classify



# --- Grabbing Comments from Reddit ---
# https://praw.readthedocs.io/en/latest/

import praw

# create a reddit instance and provide it with client_id, client_secreat and a user_agent
reddit = praw.Reddit(client_id='LK_PUjO05BqFSg', client_secret='FuE_G7UhRkvIsVNurMuo0VMO3J85ug', user_agent='scraper project')

subr = 'Reformed' # put the name of the subreddit as a string variable for ease

subreddit = reddit.subreddit(subr)

print(subreddit.display_name)
print(subreddit.title)
print(subreddit.description)

