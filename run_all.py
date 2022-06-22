import content
import clean
import sentiment
import wcloud
import pandas as pd


data_path = "/Users/philippjohn/Developer/youtube-analytics-data/"
car = "Porsche_911_GT3​"
video_id = "XdBDWTLe49g"

#-----------------------------------------------------------------------

# 1) Get content
print("")
print("1) Get content")
# 1.1) Get content
comments = content.get_content(car, video_id)

#-----------------------------------------------------------------------

# 2) Calculate sentiment
print("")
print("2) Calculate sentiment")
# 2.1) Get content
print("   2.1) Get content")
df = df = pd.read_csv(data_path + car + "/content.csv", header=[0], lineterminator='\n')

# 2.2) Clean
print("   2.2) Clean")
content_clean = clean.basic_clean(car, df)

# 2.3) Calculate sentiment
print("   2.3) Calculate sentiment")
sentiment_1 = sentiment.calculate_sentiment_transformers(car, content_clean)
sentiment_2 = sentiment.calculate_sentiment_textblob(car, sentiment_1)

#-----------------------------------------------------------------------

# 3) Generate wordcloud
print("")
print("3) Generate wordcloud")
# 3.1) Get content
print("   3.1) Get content")
df = pd.read_csv(data_path + car + "/content_clean.csv", header=[0], lineterminator='\n')

# 3.2) Clean
print("   3.2) Clean")
df_no_stopwords = clean.remove_stopwords(car=car, df=df)

# 3.3) Generate wordcloud
print("   3.3) Generate wordcloud")
wcloud.generate_wordcloud(car=car, df=df_no_stopwords)
