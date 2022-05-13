#!/usr/bin/env python
# coding: utf-8

# In[63]:


# Imports

import praw
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import datetime

# from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

# In[64]:


# Reddit Authentication for PRAW

reddit = praw.Reddit(
    client_id='LK_PUjO05BqFSg', 
    client_secret='FuE_G7UhRkvIsVNurMuo0VMO3J85ug', 
    user_agent='scraper project',
    check_for_async=False)

# Subreddit to Scrape

subr = 'Reformed'

# iterate over an array, list, etc BACKWARDS (it's faster)

# In[65]:


# Getting to the nitty gritty... 

# get the top 10 hot posts from the selected subreddit
# and print them out

# subr_posts = reddit.subreddit(subr).new(limit=10)
# for post in subr_posts:
#     print(post.title)


# In[66]:


# Get and print subreddit data

subr_data = reddit.subreddit(subr)

print(subr_data.display_name)
print(subr_data.public_description)


# In[67]:


# Let's save the scraped data into a variable so we can file it away later

posts = [] # variable initialization
comments = []

print(subr)
subr_posts = reddit.subreddit(subr).new(limit=5) # grab the most recent {limit = x} posts

for post in subr_posts: # loop through them
   
    # take a look at the title and label it 
    title_score = sia.polarity_scores(post.title)
    # posts.append([title_score]) # add the score to the post list
    
    # do the same for the selftext
    selftext_score = sia.polarity_scores(post.selftext)
    # posts.append([selftext_score]) # add the score to the posts list
    
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, title_score, selftext_score]) # build a list of those posts
    
    submission = reddit.submission(id=post.id) # with the post id, retrieve the post+comments
    submission.comments.replace_more(limit=None) # retrieve all comments for that post id
       
    for comment in submission.comments.list(): # loop through the post's comments
        
        # take a look at the comments and label them
        comment_score = sia.polarity_scores(comment.body)
        # comments.append([comment_score]) # add the score to the comment list
        
        comments.append([comment.score, comment.submission, comment.id, comment.subreddit, comment.body, comment.created, comment_score]) # build a list from those comments
        
    
comments = pd.DataFrame(comments,columns=['score', 'id','comment-id','subreddit','body','created', 'comment_score']) # transform compiled list of comments into a dataframe
    
posts = pd.DataFrame(posts,columns=['title', 'score', 'id','subreddit','url','num_comments','body','created','title_score', 'selftext_score']) # transfrom compiled list of posts into a dataframe


# In[68]:


df = pd.concat([posts, comments], ignore_index=True) # joining the posts and the comments together

df = df[['title','score','body','id','comment-id','url','num_comments','created','subreddit','title_score','selftext_score','comment_score']] # reorder columns


# In[69]:

    
df.head()


# Saving to a csv named after the subreddit

# now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

# df.to_csv(f'top_{subr}_posts_{now}.csv')
# df.to_csv('file.csv')
