import content
import clean
import sentiment
import pandas as pd


data_path = "/Users/philippjohn/Developer/youtube-analytics-data/"
car = "Pininfarina_Battista"

# 1) Get content
df = df = pd.read_csv(data_path + car + "/content.csv", header=[0], lineterminator='\n')
print(df.head())
print("")

# 2) Clean
content_clean = clean.basic_clean(car, df)
print(content_clean.head())
print("")

# 3) Get sentiment
sentiment_1 = sentiment.calculate_sentiment_transformers(car, content_clean)
print(sentiment_1.head())
print("")

sentiment_2 = sentiment.calculate_sentiment_textblob(car, sentiment_1)
print(sentiment_2.head())
print("")