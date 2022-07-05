from utils.video import Video 

#-----------------------------------------------------------------------

car = "Maserati MC20"
channel = "TopGear"
url = "https://www.youtube.com/watch?v=NMqT8YR_Al8"
features = ["rim", "steering wheel", "engine", "color", "colour",
            "carbon", "light", "design", "sound", "interior", 
            "exterior", "mirror", "body", "brake", "chassis", 
            "suspension", "gearbox", "navigation", "infotainment",
            "power", "acceleration", "handling"]

video = Video(car, channel, url, features)

#-----------------------------------------------------------------------

# 1) Get content
print("1) Get content for " + video.get_car_name())
video.get_content()

# 2) Calculate sentiment
print("2) Calculate sentiment")
video.get_sentiment()

# 3) Generate wordcloud
print("3) Generate wordcloud")
video.get_wordcloud()

# 4) Get feature stats
print("4) Get feature stats")
video.get_feature_stats()