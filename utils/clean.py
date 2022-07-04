from string import punctuation
import re
import nltk
from nltk.corpus import stopwords
import pandas as pd
import os


main_dir = os.path.dirname(__file__)
data_dir = os.path.join(main_dir, "data")

#-----------------------------------------------------------------------

# Return a df with cleaned content (remove @abc mentions, links, and 
# punctuation)

def basic_clean(car, df):
    # Creating function to clean comments
    def clean(content):
        content = re.sub(r"@[A-Za-z0-9]+", "", content)
        content = re.sub(r"https?:\/\/\S+", "", content)
        content = re.sub(r"http?:\/\/\S+", "", content)
        content = content.translate(str.maketrans("", "", punctuation))
        return content

    # Cleaning content
    df["content_clean"] = df["content"].apply(clean)

    # Write df to csv
    df.to_csv(data_dir + car + "/content_clean.csv")  

    return df

#-----------------------------------------------------------------------

# Return a df where stopwords are removed from content

def remove_stopwords(car, df):
    # Download and select stopwords
    nltk.download('stopwords')
    english_stop_words = stopwords.words('english')

    # Func which removes stopwords
    def stop_word_removal_nltk(x):
        token = x.split()
        return " ".join([w for w in token if not w in english_stop_words])

    # Remove col[0] (csv index) and NaNs
    df = df.drop(df.columns[0], axis=1)
    df = df[df["content_clean"].notnull()]

    # Remove stopwords and create new col in df
    df["content_no_stopwords"]  = df["content_clean"].apply(stop_word_removal_nltk)

    # Write df to csv
    df.to_csv(data_dir + car + "/content_no_stopwords.csv")  

    return df

#-----------------------------------------------------------------------

# Testing

def main():
    car = "Pininfarina_Battista"
    df = pd.read_csv(data_dir + car + "/content_clean.csv", header=[0])
    df = df.drop(['Unnamed: 0'], axis=1, errors='ignore')
    print(df.head())
    print("")

    df_no_stopwords = remove_stopwords(car=car, df=df)
    print(df_no_stopwords.head())
    print("")

if __name__=='__main__':
    main()