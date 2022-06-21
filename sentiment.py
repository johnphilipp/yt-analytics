import yt
from string import punctuation
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def clean_content(df):
    # Creating function to clean comments
    def clean(content):
        content = re.sub(r"@[A-Za-z0-9]+", "", content)
        content = re.sub(r"https?:\/\/\S+", "", content)
        comment = content.translate(str.maketrans("", "", punctuation))
        return content

    # Cleaning content
    df["content_clean"] = df["content"].apply(clean)

    return df

def calculate_sentiment(df):
    tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

    def sentiment_score(review):
        tokens = tokenizer.encode(review, return_tensors='pt')
        result = model(tokens)
        # result.logits # prints tensor
        return int(torch.argmax(result.logits))+1
    
    df["sentiment"] = df["content"].apply(lambda x: sentiment_score(x[:512]))

def main():
    video_id = "SMyD-Ax2Gkg"
    df = yt.get_comments_and_replies_for(video_id, offline=True)

    df_clean = clean_content(df)
    print(df_clean.head())

if __name__ == '__main__':
    main()

