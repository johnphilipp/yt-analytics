from utils import features
import pandas as pd
import os


main_dir = os.path.dirname(__file__)
data_dir = os.path.join(main_dir, "data")
car = "Porsche_911_Sport_Classic​"

df = pd.read_csv(data_dir + car + "/sentiment_1.csv", header=[0], lineterminator='\n')
df = df.drop(['Unnamed: 0'], axis=1, errors='ignore')

feature_list = ["rim", "steering wheel", "engine", "color", "colour",
            "carbon", "light", "design", "sound", "interior", 
            "exterior", "mirror", "body", "brake", "chassis", 
            "suspension", "gearbox", "navigation", "infotainment"]

df_features = features.get_features(car, df, feature_list)
df_feature_stats = features.get_feature_stats(car, df_features, feature_list)