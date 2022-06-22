from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import clean


def generate_wordcloud(car, df, file_name="wordcloud"):
    all_words = " ".join([w for w in df["content_no_stopwords"]])
    wordcloud = WordCloud(width=500, height=300, random_state=21, max_font_size=119).generate(all_words)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("data/" + car + "/" + file_name + ".jpg")

def main():
    car = "Pininfarina_Battista"

    # 1) Get content
    df = pd.read_csv("data/" + car + "/content_clean.csv", header=[0], lineterminator='\n')
    print(df.head())
    print("")

    # 2) Clean
    df_no_stopwords = clean.remove_stopwords(car, df)
    print(df_no_stopwords.head())
    print("")

    # 3) Generate wordcloud
    generate_wordcloud(car, df_no_stopwords)

if __name__=='__main__':
    main()