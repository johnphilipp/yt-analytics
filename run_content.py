from utils import content


car = "Pininfarina_Battista"
video_id = "ZfnFL-wp-dg"

# 1) Get content
comments = content.get_content(car, video_id)
print(comments.head())
print("")
