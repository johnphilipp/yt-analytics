import pandas as pd

df = pd.read_csv("/Users/philippjohn/Developer/youtube-analytics/data/Polestar_2/carwow/content_clean.csv", header=[0], lineterminator='\n')


postdata = df.to_dict()

# Assumes any auth/headers you need are already taken care of.
result = firebase.post('/my_endpoint', postdata, {'print': 'pretty'})
print(result)
# Snapshot info