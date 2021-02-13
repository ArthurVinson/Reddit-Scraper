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

# testing some capabilities of praw
# - get the most recent 15 hot posts from a subreddit

# find a relevant comment/post 
# grab comments
# parse the comments/clean the data for NLP


sub = 'ffxiv'

# categorize by 'hot' posts
# hot_posts = reddit.subreddit(sub).hot(limit=15)
# for post in hot_posts:
#    print(post.title)

# categorize by 'new' posts

new_posts = reddit.subreddit(sub).new(limit=15)
for post in new_posts:
    print(post.title)

# stuff to do - go over the reference document, look at a sentiment analysis tutorial

# current project is to scrape reddit for [topic] and see what people feel about [topic]
# current subreddit-topic pairs: reformed-baptists, [unknown]-artificial meat, rats-rats
# * need to be able to scrape a subreddit, not just most recent but all
# * grab comments (not just top level but all)

# future project will scrape (all of) reddit ( for a keyword or key phrase and conduct sentiment analysis on comments it finds