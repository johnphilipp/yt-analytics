import content
import clean
import sentiment
import pandas as pd
import os


main_dir = os.path.dirname(__file__)
data_dir = os.path.join(main_dir, "data")
car = "Pininfarina_Battista"

# 1) Get content
df = df = pd.read_csv(data_dir + car + "/content.csv", header=[0], lineterminator='\n')
df = df.drop(['Unnamed: 0'], axis=1, errors='ignore')
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