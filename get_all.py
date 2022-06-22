import content
import clean
import sentiment
import wcloud
import pandas as pd


car = "Porsche_911_SC"
video_id = "mmzn77xOCe0"

#-----------------------------------------------------------------------

# 1) GET CONTENT
# 1.1) Get content
comments = content.get_content(car, video_id)
print(comments.head())
print("")

#-----------------------------------------------------------------------

# 2) CALCULATE SENTIMENT
# 2.1) Get content
df = content.get_content(car, offline=True)
print(df.head())
print("")

# 2.2) Clean
content_clean = clean.basic_clean(car, df)
print(content_clean.head() + "\n")
print("")

# 2.3) Get sentiment
sentiment_1 = sentiment.calculate_sentiment_transformers(car, content_clean)
print(sentiment_1.head())
print("")

sentiment_2 = sentiment.calculate_sentiment_textblob(car, sentiment_1)
print(sentiment_2.head())
print("")

#-----------------------------------------------------------------------

# 3) GENERATE WORDCLOUD
# 3.1) Get content
print('1) Get content')
print('--------------------')
df = pd.read_csv("data/" + car + "/content_clean.csv", header=[0], lineterminator='\n')
print(df.head())
print("")

# 3.2) Clean
print('2) Clean')
print('--------------------')
df_no_stopwords = clean.remove_stopwords(car=car, df=df)
print(df_no_stopwords.head())
print("")

# 3.3) Generate wordcloud
print('3) Generate wordcloud')
print('--------------------')
wcloud.generate_wordcloud(car=car, df=df_no_stopwords)
