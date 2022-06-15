import module
import os
import googleapiclient.discovery
from operator import itemgetter

def main():
    rawData = module.get_data_for_video("2CY-S1Z_I38")

    # commentStats: [commentId, nLikes, nComments]
    commentStats = module.get_comment_stats(rawData) 
    commentStats = sorted(commentStats, key=itemgetter(1), reverse=True)
    for i in range(len(commentStats)):
        print(commentStats[i])
        if i == 100:
            break

    # commentReplyData: [commentId, replyId, content]
    commentReplyData = module.get_comments_and_replies(rawData)
    commentReplyData = sorted(commentReplyData, key=itemgetter(1), reverse=True)
    for i in range(len(commentReplyData)):
        print(commentReplyData[i])
        if i == 100:
            break
    print("")
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