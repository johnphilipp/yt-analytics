import clean
import wcloud
import pandas as pd
import os


main_dir = os.path.dirname(__file__)
data_dir = os.path.join(main_dir, "data")
car = "Pininfarina_Battista"

# 1) Get content
print('1) Get content')
print('--------------------')
df = pd.read_csv(data_dir + car + "/content_clean.csv", header=[0], lineterminator='\n')
df = df.drop(['Unnamed: 0'], axis=1, errors='ignore')
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
