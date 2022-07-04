import pandas as pd
import os


main_dir = os.path.dirname(__file__)
data_dir = os.path.join(main_dir, "data")

#-----------------------------------------------------------------------

# Return df which filters to only include content that contains meantion 
# of a feature

def get_features(car, df, feature_list):
    # Remove NaNs
    df = df[df["content_clean"].notnull()]

    # Func which returns df of a single feature
    def get_single_feature(df, feature):
        df_single_feature = pd.DataFrame()
        df_single_feature = pd.concat([df_single_feature, df[df["content_clean"].str.lower().str.contains(feature)]], axis=0)
        df_single_feature["feature"] = feature
        return df_single_feature

    # Stitch df_single_feature together into df_features
    df_features = pd.DataFrame()
    for feature in feature_list:
        df_features = pd.concat([df_features, get_single_feature(df, feature)], axis=0)
    
    # Write df
    df.to_csv(data_dir + car + "/features.csv")  

    return df_features


def get_feature_stats(car, df_features, feature_list):
    df_feature_stats = []
    for feature in feature_list:
        df_feature_stats.append([feature,
                                 len(df_features[df_features["feature"] == feature]),
                                 df_features[df_features["feature"] == feature]["sentiment"].mean()])

    df_feature_stats = pd.DataFrame(df_feature_stats, columns=['feature', 'comment_count', 'sentiment_mean'])
    df_feature_stats = df_feature_stats[df_feature_stats['comment_count'] >= 1]  
    df_feature_stats = df_feature_stats.sort_values(by=["sentiment_mean"], ascending=False)
    df_feature_stats = df_feature_stats.reset_index(drop=True)

    # Write df
    df_feature_stats.to_csv(data_dir + car + "/feature_stats.csv")  

    return df_feature_stats

#-----------------------------------------------------------------------

# Testing

def main():
    car = "Porsche_911_GT3​"
    df = pd.read_csv(data_dir + car + "/sentiment_1.csv", header=[0], lineterminator='\n')
    df = df.drop(['Unnamed: 0'], axis=1, errors='ignore')

    feature_list = ["rim", "steering wheel", "engine", "color", "colour",
                "carbon", "light", "design", "sound", "interior", 
                "exterior", "mirror", "body", "brake", "chassis", 
                "suspension", "gearbox", "navigation", "infotainment"]
    
    df_features = get_features(car, df, feature_list)
    df_feature_stats = get_feature_stats(car, df_features, feature_list)

if __name__ == '__main__':
    main()