import content
import clean
import sentiment


car = "Pininfarina_Battista"

# 1) Get content
df = content.get_content(car, offline=True)
print(df.head())
print("")

# 2) Clean
content_clean = clean.basic_clean(car, df)
print(content_clean.head() + "\n")
print("")

# 3) Get sentiment
sentiment_1 = sentiment.calculate_sentiment_transformers(car, content_clean)
print(sentiment_1.head())
print("")

sentiment_2 = sentiment.calculate_sentiment_textblob(car, sentiment_1)
print(sentiment_2.head())
print("")