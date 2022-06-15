# -*- coding: utf-8 -*-

# Sample Python code for youtube.comments.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import json
import googleapiclient.discovery
import script

def get_comments_and_replies(data):
    a = []
    n_comments = 0
    for set in data:
        for i in range(int(len(set["items"]))):
            a.append([
                [n_comments], 
                [0], 
                [set["items"][i]["snippet"]["topLevelComment"]["snippet"]["textDisplay"]]
            ])
            if set["items"][i].get("replies") != None: 
                for j in range(len(set["items"][i]["replies"]["comments"])):
                    a.append([
                        [n_comments], 
                        [j+1], 
                        [set["items"][i]["replies"]["comments"][j]["snippet"]["textDisplay"]]
                    ])
            n_comments += 1
    return a

def get_comment_stats(data):
    a = []
    n_comments = 0
    for set in data:
        for i in range(int(len(set["items"]))):
            a.append([
                [n_comments], 
                [set["items"][i]["snippet"]["topLevelComment"]["snippet"]["likeCount"]], 
                [set["items"][i]["snippet"]["totalReplyCount"]]
            ])
            n_comments += 1
    return a

def get_data_for_video(videoId):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDtuq5QvhIxQFpZTSqYIQ7Hs2bSWhNyW0Y"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    # Query
    data = {}
    dataAll = []
    comments_and_replies = [] # [commentId, replyId, content]
    comment_stats = [] # [commentId, nLikes, nComments]
    nextPageToken = None
    page = 0
    while data.get("nextPageToken") != None or nextPageToken == None:
        request = youtube.commentThreads().list(
            part="snippet, replies",
            videoId=videoId,
            maxResults=100, # max 100
            textFormat="plainText",
            order="relevance",
            pageToken=nextPageToken # None at first iteration
        )
    
        # Execute request
        data = request.execute()
        dataAll.append(data)

        # # Print data as raw son
        # # print(json.dumps(data, indent=2))

        # # Call comments_and_replies and concatenate
        # comments_and_replies += module.get_comments_and_replies(data, len(comments_and_replies))

        # # Call comment_stats and concatenate
        # comment_stats += module.get_comment_stats(data, len(comment_stats))

        # Get next pageToken in new_data
        if data.get("nextPageToken") != None:
            nextPageToken = data["nextPageToken"]
        
        page += 1
        # print(page)

    return dataAll


def main():
    a = True

    # # Print filtered_data
    # for i in comments_and_replies:
    #     print(i)
    
    # # Print comment_stats
    # for i in comment_stats:
    #     print(i)

    # # Words with relevance (grouped)
    # suggestion = ["suggest", "you", "think"]
    # negative = ["bad"] # check cases like "not great"
    # positive = ["great", "amazing", "love", "well done", "best"]
        

if __name__ == "__main__":
    main()