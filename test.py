# -*- coding: utf-8 -*-

# Sample Python code for youtube.comments.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import json
import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDtuq5QvhIxQFpZTSqYIQ7Hs2bSWhNyW0Y"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet, replies",
        videoId="8pbLytVTM9o",
        maxResults=10, # max 100
        textFormat="plainText",
        order="relevance"
    )
    
    response = request.execute()

    print(json.dumps(response, indent=2))
    print("") 

    data  = json.loads(json.dumps(response, indent=2))
    for i in range(int(len(data["items"]))):
        print(str(i) + " " + data["items"][i]["snippet"]["topLevelComment"]["snippet"]["textDisplay"])
        if data["items"][i].get("replies") != None: 
            for j in range(len(data["items"][i]["replies"]["comments"])):
                print("  " + str(i) + "." + str(j) + " " + data["items"][i]["replies"]["comments"][j]["snippet"]["textDisplay"])
        print("")
        

if __name__ == "__main__":
    main()