# -*- coding: utf-8 -*-
"""
PSAW powered Reddit Dataset Scraper -

The end goal is a set of functions which join together the functionality of 
Reddit Scraping.py and datasetcompile.py into a better looking solution that
has more personal creativity than a copy and paste.

Created on Thu May 26 15:19:02 2022

From https://towardsdatascience.com/how-to-collect-a-reddit-dataset-c369de539114

@author: Arthur Vinson
"""

import pandas as pd
import datetime as dt
import os

import praw
from psaw import PushshiftAPI

# to use PSAW (initializing the API)
api = PushshiftAPI()

# to use PRAW (reddit credentials)
reddit = praw.Reddit(
    client_id='LK_PUjO05BqFSg', 
    client_secret='FuE_G7UhRkvIsVNurMuo0VMO3J85ug', 
    user_agent='scraper project',
    check_for_async=False)


# subreddits = ['Pathfinder2e','MouseGuard','Pathfinder_RPG','DnD','CallofCthulhu','shadowrun']

subreddits = ['Pathfinder_RPG']
start_year = 2019
end_year = 2022

# directory on which to store the data
basecorpus = './my-dataset/'

import time

# the log_action function helps to debug by documenting various info and printing it to screen
# can be used to print to file instead (task to do)
def log_action(action):
    print(action)
    return

"""
Main Algorithm 

For each year between start_year and end_year, create a directory
For each subreddit in subreddits create a directory to store that subreddit's 
post during that year
"""

""" 
BLOCK 1

For each year between start_year and end_year, create a directory and define 
the beginning and ending timestamps (as epochs) to be used in the PSAW request.

"""
 
# For each year between start_year and end_year  
for year in range(start_year, end_year+1):
    action = "[Year] " + str(year)
    log_action(action)

    # create a directory
    dirpath = basecorpus + str(year)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    # define the beginning and ending timestamps that describe window of posts
    # these are used to provide input to the PSAW request
    ts_after = int(dt.datetime(year, 1, 1).timestamp())
    ts_before = int(dt.datetime(year+1, 1, 1).timestamp())
        
    #task to do - allow for arbitrary ranges instead of years by using epochs directly


# =============================================================================
# BLOCK 2 
# 
# For each subreddit in subreddits, create the corresponding directory inside
# the # current year's directory, and define the path for the CSV file to store
# the # corresponding posts
# =============================================================================

    # for each subreddit in subreddits
    for subreddit in subreddits:
        start_time = time.time() # start logging time for log_action

        action = "\t[Subreddit] " + subreddit
        log_action(action)

        # create corresponding directory inside current year's directory
        subredditdirpath = dirpath + '/' + subreddit
        if os.path.exists(subredditdirpath): # if the file exists
            continue # move on
        else: # otherwise
            os.makedirs(subredditdirpath) # create the directory

        # define the CSV path to store corresponding posts
        submissions_csv_path = str(year) + '-' + subreddit + '-submissions.csv'
        
# =============================================================================
# 
# BLOCK 3 
# 
# Define the Python dictionary on which each post will be stored in memory, to
# be later saved to the CSV file defined. 
# 
# =============================================================================

        submissions_dict = {
            "id" : [],
            "url" : [],
            "title" : [],
            "score" : [],
            "num_comments": [],
            "created_utc" : [],
            "selftext" : [],
        }

# task to do - adopt naming scheme from Reddit Scraping.py

# =============================================================================
#  
# BLOCK 4
# 
# Use PSAW to get the submissions id of a specific set of posts: those that 
# exist with the starting and ending times, in the specific subreddit. Also
# limit the number retrieved to limit. Use the Python keyword None to go over
# all posts in the time frame
#
# =============================================================================

        # use PSAW to get id of submissions in time interval
        # first create an iterator
        gen = api.search_submissions(
            after=ts_after, # beginning timestamp
            before=ts_before, # ending timestamp
            filter=['id'], # only get the id, nothing else
            subreddit=subreddit, # specific subreddit
            limit=None # how many to retrieve in the time frame
        )

# =============================================================================
# 
# BLOCK 5
# 
# For each post or submission in the iterator, use the id we retrieved to get
# the full data we want from PRAW and add it to the dictionary.
# 
# =============================================================================

        # use PRAW to get actual info and traverse comment tree
        # for every submission in the iterator gen
        for submission_psaw in gen:
            # get the id from psaw
            submission_id = submission_psaw.d_['id']
            # use the id in praw to get full data
            submission_praw = reddit.submission(id=submission_id)

            submissions_dict["id"].append(submission_praw.id)
            submissions_dict["url"].append(submission_praw.url)
            submissions_dict["title"].append(submission_praw.title)
            submissions_dict["score"].append(submission_praw.score)
            submissions_dict["num_comments"].append(submission_praw.num_comments)
            submissions_dict["created_utc"].append(submission_praw.created_utc)
            submissions_dict["selftext"].append(submission_praw.selftext)

# =============================================================================
#
# BLOCK 6
# 
# Each submission has a resulting comment thread. Define the file path to a CSV
# for the comment thread. Define the dictionary to store comment thread data.
# 
# =============================================================================

            submission_comments_csv_path = str(year) + '-' + subreddit + '-submission_' + submission_id + '-comments.csv'
            submission_comments_dict = {
                "comment_id" : [],
                "comment_parent_id" : [],
                "comment_body" : [],
                "comment_link_id" : [],
                "comment_created" : []
            }

# =============================================================================
# 
# BLOCK 7
# 
# For each comment in the comment thread, retrieve the data and store it in the
# dictionary defined. Save it to the CSV file.
# 
# =============================================================================

            # extend the comment tree all the way
            submission_praw.comments.replace_more(limit=None)
            # for each comment in flattened comment tree
            for comment in submission_praw.comments.list():
                submission_comments_dict["comment_id"].append(comment.id)
                submission_comments_dict["comment_parent_id"].append(comment.parent_id)
                submission_comments_dict["comment_body"].append(comment.body)
                submission_comments_dict["comment_link_id"].append(comment.link_id)
                submission_comments_dict["comment_created"].append(comment.created)

            # for each submission save separate csv comment file
            pd.DataFrame(submission_comments_dict).to_csv(subredditdirpath + '/' + submission_comments_csv_path,
                                                          index=False)

# =============================================================================
# 
# BLOCK 8
# 
# Save the constructed dictionary of all the submissions to a CSV file
#  
# =============================================================================
        # single csv file with all submissions
        pd.DataFrame(submissions_dict).to_csv(subredditdirpath + '/' + submissions_csv_path,
                                              index=False)

# log the actions 

        action = f"\t\t[Info] Found submissions: {pd.DataFrame(submissions_dict).shape[0]}"
        log_action(action)

        action = f"\t\t[Info] Elapsed time: {time.time() - start_time: .2f}s"
        log_action(action)