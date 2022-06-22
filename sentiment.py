import content
import clean
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from textblob import TextBlob
import pandas as pd


data_path = "/Users/philippjohn/Developer/youtube-analytics-data/"

#-----------------------------------------------------------------------

# Return a df with sentiment score based on transformers

def calculate_sentiment_transformers(car, df):
    # Initiate model
    tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

    def sentiment_score(review):
        tokens = tokenizer.encode(review, return_tensors='pt')
        result = model(tokens)
        # result.logits # prints tensor
        return int(torch.argmax(result.logits))+1
    
    # Claculate sentiment
    df["sentiment"] = df["content_clean"].apply(lambda x: sentiment_score(x[:512]))

    # Write df to csv
    df.to_csv(data_path + car + "/sentiment_1.csv")  

    return df

#-----------------------------------------------------------------------

# Return a df with sentiment score (subjectivity and polarity) based on 
# textblob

def calculate_sentiment_textblob(car, df):
    # Create func to get subjectivity
    def get_subjectivity(text):
        return TextBlob(text).sentiment.subjectivity

    # Create func to get polarity
    def get_polarity(text):
        return TextBlob(text).sentiment.polarity

    # Create two new cols
    df["subjectivity"] = df["content_clean"].apply(get_subjectivity)
    df["polarity"] = df["content_clean"].apply(get_polarity)

    # Create func to compute pos, neg, neutr
    def get_analysis(score):
        if score < 0:
            return "Negative"
        elif score == 0:
            return "Neutral"
        else:
            return "Positive"

    # Create new col
    df["analysis"] = df["polarity"].apply(get_analysis)

    # Write df to csv
    df.to_csv(data_path + car + "/sentiment_2.csv")  

    return df

#-----------------------------------------------------------------------

# Testing

def main():
    car = "Pininfarina_Battista"

    # 1) Get content
    print('1) Get content')
    print('--------------------')
    df = df = pd.read_csv(data_path + car + "/content.csv", header=[0], lineterminator='\n')
    print(df.head())
    print("")

    # 2) Clean
    print('2) Clean')
    print('--------------------')
    df_clean = clean.basic_clean(car, df)
    print(df_clean.head())
    print("")

    # 3) Get sentiment
    print('3) Get sentiment')
    print('--------------------')
    sentiment_1 = calculate_sentiment_transformers(car, df_clean)
    print(sentiment_1.head())
    print("")

    sentiment_2 = calculate_sentiment_textblob(car, sentiment_1)
    print(sentiment_2.head())
    print("")

if __name__ == '__main__':
    main()

