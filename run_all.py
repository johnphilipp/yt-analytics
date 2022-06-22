import content
import clean
import sentiment
import wcloud
import pandas as pd


data_path = "/Users/philippjohn/Developer/youtube-analytics-data/"
car = "Porsche_911_Sport_Classic​"
video_id = "mmzn77xOCe0"

#-----------------------------------------------------------------------

# 1) GET CONTENT
print("")
print("1) Get content")
# 1.1) Get content
comments = content.get_content(car, video_id)

#-----------------------------------------------------------------------

# 2) CALCULATE SENTIMENT
print("")
print("2) Calculate sentiment")
# 2.1) Get content
print("  2.1) Calculate sentiment")
df = df = pd.read_csv(data_path + car + "/content.csv", header=[0], lineterminator='\n')

# 2.2) Clean
print("  2.2) Clean")
content_clean = clean.basic_clean(car, df)

# 2.3) Calculate sentiment
print("  2.3) Calculate sentiment")
sentiment_1 = sentiment.calculate_sentiment_transformers(car, content_clean)
sentiment_2 = sentiment.calculate_sentiment_textblob(car, sentiment_1)

#-----------------------------------------------------------------------

# 3) GENERATE WORDCLOUD
print("")
print("2) Calculate sentiment")
# 3.1) Get content
print("  2.1) Get content")
df = pd.read_csv(data_path + car + "/content_clean.csv", header=[0], lineterminator='\n')
print(df.head())
print("")

# 3.2) Clean
print("  2.2) Clean")
print('--------------------')
df_no_stopwords = clean.remove_stopwords(car=car, df=df)
print(df_no_stopwords.head())
print("")

# 3.3) Generate wordcloud
print("  2.3) Generate wordcloud")
wcloud.generate_wordcloud(car=car, df=df_no_stopwords)
