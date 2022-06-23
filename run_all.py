from utils import content
from utils import clean
from utils import sentiment
from utils import wcloud
from utils import features
import pandas as pd


data_path = "/Users/philippjohn/Developer/youtube-analytics-data/"
car = "Porsche_911_Carrera_S__Top_Gear" 
video_id = "SjrarcM7HoY" 

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
df = pd.read_csv(data_path + car + "/content.csv", header=[0], lineterminator='\n')
df = df.drop(['Unnamed: 0'], axis=1, errors='ignore')

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
df = df.drop(['Unnamed: 0'], axis=1, errors='ignore')

# 3.2) Clean
print("   3.2) Clean")
df_no_stopwords = clean.remove_stopwords(car=car, df=df)

# 3.3) Generate wordcloud
print("   3.3) Generate wordcloud")
wcloud.generate_wordcloud(car=car, df=df_no_stopwords)

#-----------------------------------------------------------------------

# 4) Get feature stats
print("")
print("4) Get feature stats")

# 4.1) Get content
print("   4.1) Get content")
df = pd.read_csv(data_path + car + "/sentiment_1.csv", header=[0], lineterminator='\n')
df = df.drop(['Unnamed: 0'], axis=1, errors='ignore')

feature_list = ["rim", "steering wheel", "engine", "color", "colour",
            "carbon", "light", "design", "sound", "interior", 
            "exterior", "mirror", "body", "brake", "chassis", 
            "suspension", "gearbox", "navigation", "infotainment"]

# 4.2) Get features
print("   4.2) Get features")
df_features = features.get_features(car, df, feature_list)

# 4.3) Get feature stats
print("   4.3) Get feature stats")
df_feature_stats = features.get_feature_stats(car, df_features, feature_list)
