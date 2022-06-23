import plotly.express as px
import pandas as pd


data_path = "/Users/philippjohn/Developer/youtube-analytics-data/"

#-----------------------------------------------------------------------

# Generate and a radar chart using plotly.express

def get_radar_chart(cars):
  # Get dfs
  df = pd.DataFrame()

  if len(cars) == 0:
      print("Please input at least one car")
  else:
      for car in cars:
          df_car = pd.read_csv(data_path + car + "/feature_stats.csv", lineterminator='\n')
          df_car = df_car.drop(['Unnamed: 0'], axis=1, errors='ignore')
          df_car['car'] = car
          df = pd.concat([df, df_car])

  df = df.reset_index(drop=True)
  df = df[df.groupby('feature')["feature"].transform(len) > (len(cars) - 1)]
  df = df.sort_values(by=['feature'])
  df.insert(0, 'car', df.pop('car'))
  print(df.head(n=100))

  # Assemble fig
  fig = px.line_polar(df, r='sentiment_mean', theta='feature', color='car', line_close=True,
                      line_shape='linear',  # or spline
                      hover_name='car',
                      hover_data={'car':False},
                      markers=True,
                      # labels={'rating':'stars'},
                      # text='car',
                      # start_angle=0,
                      range_r=[0,5],
                      direction='clockwise'  # or counterclockwise
                      )
  fig.update_traces(fill='toself')
  fig.show()

#-----------------------------------------------------------------------

# Testing

def main():
  cars = ["Porsche_911_GT3​",
        "Porsche_911_Sport_Classic​",
        "BMW_M3_Touring"]
  
  get_radar_chart(cars)

if __name__ == '__main__':
  main()