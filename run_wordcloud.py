import clean
import wcloud
import pandas as pd


data_path = "/Users/philippjohn/Developer/youtube-analytics-data/"
car = "Pininfarina_Battista"

# 1) Get content
print('1) Get content')
print('--------------------')
df = pd.read_csv(data_path + car + "/content_clean.csv", header=[0], lineterminator='\n')
print(df.head())
print("")

# 2) Clean
print('2) Clean')
print('--------------------')
df_no_stopwords = clean.remove_stopwords(car=car, df=df)
print(df_no_stopwords.head())
print("")

# 3) Generate wordcloud
print('3) Generate wordcloud')
print('--------------------')
wcloud.generate_wordcloud(car=car, df=df_no_stopwords)
