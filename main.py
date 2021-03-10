# Reddit Scraper
# Arthur Vinson
# 2/8/2021

# This scraper will do the following:
# 1. Grab a collection of reddit comments from a selected subreddit using PRAW
# 2. Perform sentiment analysis. 

# Simple, no?

# Your task is to split posts into sentences, tag them with a PoS tagger that we will provide, gather some
# feature information from each post, learn models, and use these to classify

# Comment added: 2/23/2021
# 
# Do these three things
# 1. Scrape all comments from a given reddit thread
# 2. Extract the top level comments
# 3. Save to a csv file

# --- Grabbing Comments from Reddit ---
# https://praw.readthedocs.io/en/latest/

# https://towardsdatascience.com/scraping-reddit-with-praw-76efc1d1e1d9

import praw
import numpy as np
from pandas import DataFrame
from textblob import TextBlob


# create a reddit instance and provide it with client_id, client_secreat and a user_agent
reddit = praw.Reddit(client_id='LK_PUjO05BqFSg', client_secret='FuE_G7UhRkvIsVNurMuo0VMO3J85ug', user_agent='scraper project')

subr = 'Reformed' # put the name of the subreddit as a string variable for ease

# uniq_id = 'lqms6k' # unique id for the thread

# submission = reddit.submission(id=uniq_id)


# submission.comments.replace_more(limit=None)
# for top_level_comment in submission.comments:
#     print(top_level_comment.body)


# submission.comments.replace_more(limit=None)
# for comment in submission.comments.list():
#     print(comment.body)


# subreddit = reddit.subreddit(subr)

# print(subreddit.display_name)
# print(subreddit.title)
# print(subreddit.description)

# something here

# I need to talk with a duck about how to go about doing things

import pprint

sub = reddit.subreddit(subr)
# hot_python = sub.hot(limit=1)

# print(sub.display_name)

# print(sub.title)

# print(sub.description)

example = []

for submission in sub.new(limit=1):
    
    newlist = []
    
    # make a list of the different submissions and their info
    # which info is most important? 
    
    newlist.append(submission.title)
    newlist.append(submission.score)
    newlist.append(submission.selftext)
    newlist.append(submission.id)
    newlist.append(submission.url)
    
    example.append(newlist) #make a list of those lists
    
    
blob = TextBlob(submission.title)    
print(blob)

print(blob.sentiment)
    
    
# turn the list of lists into a dataframe
labels = ['Title', 'Score','text', 'id', 'URL']
df = DataFrame(example, columns=labels)

print(df)

# turn the dataframe into a CSV

fname = subr + 'data'
df.to_csv(fname, index=False, encoding='utf-8')



# run sentiment analysis on the titles 


# run sentiment analysis on the submission body


# =============================================================================
# What I'd like to do is for each submission, run sentiment analysis on each
# the comments under each and give a summary sentiment of the entire sumbission
# post and comments.  
# =============================================================================
    
    
    # print(submission.title)
    # print(submission.score)
    # print(submission.id)
    # print(submission.url)

# print(example)

# for submissions in hot_python:
#     if submissions.stickied:
#         print('Title: {}, ups: {}, downs: {}'.format(submissions.title, submissions.ups,submissions.downs))
#         post = {}
#         postlist = []                                                 
#         submissions.comments.replace_more(limit=0)
#         for comment in submissions.comments: 
#             post = {}
#             post['Author'] = comment.author
#             post['Comment'] = comment.body
#             post['Score'] = comment.score
#             postlist.append(post)
# Postdf = pd.DataFrame(postlist)