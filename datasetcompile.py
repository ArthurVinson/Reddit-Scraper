# -*- coding: utf-8 -*-
"""
PSAW powered Reddit Dataset Scraper

Created on Thu May 26 15:19:02 2022

From https://towardsdatascience.com/how-to-collect-a-reddit-dataset-c369de539114

@author: Arthur Vinson
"""

import pandas as pd
import datetime as dt
import os

import praw
from psaw import PushshiftAPI

# to use PSAW
api = PushshiftAPI()

# to use PRAW
reddit = praw.Reddit(
    client_id='LK_PUjO05BqFSg', 
    client_secret='FuE_G7UhRkvIsVNurMuo0VMO3J85ug', 
    user_agent='scraper project',
    check_for_async=False)


# subreddits = ['Pathfinder2e','MouseGuard','Pathfinder_RPG','DnD','CallofCthulhu','shadowrun']

subreddits = ['Pathfinder2e']
start_year = 2020
end_year = 2021

# directory on which to store the data
basecorpus = './my-dataset/'

import time

def log_action(action):
    print(action)
    return

### BLOCK 1 ###

for year in range(start_year, end_year+1):
    action = "[Year] " + str(year)
    log_action(action)

    dirpath = basecorpus + str(year)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    # timestamps that define window of posts
    ts_after = int(dt.datetime(year, 1, 1).timestamp())
    ts_before = int(dt.datetime(year+1, 1, 1).timestamp())

### BLOCK 2 ###

    for subreddit in subreddits:
        start_time = time.time()

        action = "\t[Subreddit] " + subreddit
        log_action(action)

        subredditdirpath = dirpath + '/' + subreddit
        if os.path.exists(subredditdirpath):
            continue
        else:
            os.makedirs(subredditdirpath)

        submissions_csv_path = str(year) + '-' + subreddit + '-submissions.csv'
        
### BLOCK 3 ###

        submissions_dict = {
            "id" : [],
            "url" : [],
            "title" : [],
            "score" : [],
            "num_comments": [],
            "created_utc" : [],
            "selftext" : [],
        }

### BLOCK 4 ###

        # use PSAW only to get id of submissions in time interval
        gen = api.search_submissions(
            after=ts_after,
            before=ts_before,
            filter=['id'],
            subreddit=subreddit,
            limit=20
        )

### BLOCK 5 ###

        # use PRAW to get actual info and traverse comment tree
        for submission_psaw in gen:
            # use psaw here
            submission_id = submission_psaw.d_['id']
            # use praw from now on
            submission_praw = reddit.submission(id=submission_id)

            submissions_dict["id"].append(submission_praw.id)
            submissions_dict["url"].append(submission_praw.url)
            submissions_dict["title"].append(submission_praw.title)
            submissions_dict["score"].append(submission_praw.score)
            submissions_dict["num_comments"].append(submission_praw.num_comments)
            submissions_dict["created_utc"].append(submission_praw.created_utc)
            submissions_dict["selftext"].append(submission_praw.selftext)

### BLOCK 6 ###

            submission_comments_csv_path = str(year) + '-' + subreddit + '-submission_' + submission_id + '-comments.csv'
            submission_comments_dict = {
                "comment_id" : [],
                "comment_parent_id" : [],
                "comment_body" : [],
                "comment_link_id" : [],
            }

### BLOCK 7 ###

            # extend the comment tree all the way
            submission_praw.comments.replace_more(limit=None)
            # for each comment in flattened comment tree
            for comment in submission_praw.comments.list():
                submission_comments_dict["comment_id"].append(comment.id)
                submission_comments_dict["comment_parent_id"].append(comment.parent_id)
                submission_comments_dict["comment_body"].append(comment.body)
                submission_comments_dict["comment_link_id"].append(comment.link_id)

            # for each submission save separate csv comment file
            pd.DataFrame(submission_comments_dict).to_csv(subredditdirpath + '/' + submission_comments_csv_path,
                                                          index=False)

### BLOCK 8 ###

        # single csv file with all submissions
        pd.DataFrame(submissions_dict).to_csv(subredditdirpath + '/' + submissions_csv_path,
                                              index=False)


        action = f"\t\t[Info] Found submissions: {pd.DataFrame(submissions_dict).shape[0]}"
        log_action(action)

        action = f"\t\t[Info] Elapsed time: {time.time() - start_time: .2f}s"
        log_action(action)