import os
import googleapiclient.discovery
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import torch
from textblob import TextBlob


#-----------------------------------------------------------------------

# Return a list with comment data for a yt video

def get_comments_for(vid):
    # -*- coding: utf-8 -*-

    # Sample Python code for youtube.comments.list
    # See instructions for running these code samples locally:
    # https://developers.google.com/explorer-help/code-samples#python

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Setup
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDtuq5QvhIxQFpZTSqYIQ7Hs2bSWhNyW0Y"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    # Query to retrieve top level comments
    def make_comments_request(vid, pToken):
        request = youtube.commentThreads().list(
            part="snippet, replies",
            videoId=vid,
            maxResults=100, # max 100
            textFormat="plainText",
            order="relevance",
            pageToken=pToken
        )
        return request.execute()

    # Retrieve first page
    comments = []
    pageToken = None # At first API call, pageToken is None
    page = make_comments_request(vid, pageToken)
    comments.append(page)
    pageToken = page.get("nextPageToken")

    # Retrieve successive page(s) if new pageToken
    while pageToken is not None:
        page = make_comments_request(vid, pageToken)
        comments.append(page)
        pageToken = page.get("nextPageToken")
    
    return comments

#-----------------------------------------------------------------------

# Return a list with reply data for a list of comments

def get_replies_for(comments):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Setup
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDtuq5QvhIxQFpZTSqYIQ7Hs2bSWhNyW0Y"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
    
    # Get ids of top level comments which have replies
    ids = []
    for page in comments:
        for i in range(int(len(page["items"]))):
            if page["items"][i].get("replies") != None: 
                ids.append(page["items"][i]["id"])

    # Query to retrieve replies on top level comments
    def make_replies_request(id, pToken):
        request = youtube.comments().list(
            part="snippet",
            parentId=id,
            maxResults=100, # max 100
            pageToken=pToken,
            textFormat="plainText"
        )
        return request.execute()

    replies = []
    for i in range(len(ids)):
        # Retrieve first page
        pageToken = None # At first API call, pageToken is None
        page = make_replies_request(ids[i], pageToken)
        replies.append(page)
        pageToken = page.get("nextPageToken")

        # Retrieve successive page(s) if new pageToken
        while pageToken is not None:
            page = make_replies_request(ids[i], pageToken)
            replies.append(page)
            pageToken = page.get("nextPageToken")
    
    return replies   

#-----------------------------------------------------------------------

# Return a df with filtered and stitched comment and reply data for a 
# video id

def get_comments_and_replies_for(vid):
    # Get comments and replies data for video id
    comments = get_comments_for(vid)
    replies = get_replies_for(comments)

    # Filter and stitch comments and replies
    data = []
    # Filter and stitch comments (append comment id and comment content)
    for page_c in comments:
        for i in range(int(len(page_c["items"]))):
            comment_id = page_c["items"][i]["id"]
            comment = page_c["items"][i]["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            data.append([comment_id, comment])

            # Fetch replies (append comment id and reply content)
            if page_c["items"][i].get("replies") != None: 
                for page_r in replies:
                    for j in range(int(len(page_r["items"]))):
                        reply_parent_id = page_r["items"][j]["snippet"]["parentId"]
                        reply_id = page_r["items"][j]["id"]
                        reply = page_r["items"][j]["snippet"]["textDisplay"]
                        if reply_parent_id == comment_id:
                            data.append([reply_id, reply])

    # Filter and stitch a df with named cols
    df = pd.DataFrame(np.array(data), columns=["id", "comment_reply"])

    return df

#-----------------------------------------------------------------------

# Testing

def main():
    video_id = "SMyD-Ax2Gkg"

    print('1) Get comments')
    print('--------------------')
    comments = get_comments_for(video_id)
    print("Pages in comments: " + str(len(comments)))
    print("")

    print('2) Get replies')
    print('--------------------')
    replies = get_replies_for(comments)
    print("Pages in replies: " + str(len(replies)))
    print("")
    
    print('3) Get df')
    print('--------------------')
    df = get_comments_and_replies_for(video_id)
    print(df.head())
        
if __name__ == "__main__":
    main()