import streamlit as st
import plotly.express as px
import pandas as pd

# https://github.com/streamlit/example-app-commenting/blob/main/utils/chart.py
# https://share.streamlit.io/streamlit/example-app-commenting/main

data_path = "/Users/philippjohn/Developer/youtube-analytics-data/"

def merge_df(cars):
    # Get and merge dfs
    df = pd.DataFrame()
    for car in cars:
        df_car = pd.read_csv(data_path + car + "/feature_stats.csv", lineterminator='\n')
        df_car = df_car.drop(['Unnamed: 0'], axis=1, errors='ignore')
        df_car['car'] = car
        df = pd.concat([df, df_car])

    df = df.reset_index(drop=True)
    df = df[df.groupby('feature')["feature"].transform(len) > (len(cars) - 1)]
    df = df.sort_values(by=['feature'])
    df.insert(0, 'car', df.pop('car'))

    return df

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

def radar_chart(df):  
    fig = px.line_polar(df, 
                        r='sentiment_mean', 
                        theta='feature', 
                        color='car', 
                        line_close=True,
                        line_shape='linear',  # or spline
                        hover_name='car',
                        hover_data={'car':False},
                        markers=True,
                        # labels={'rating':'stars'},
                        # text='car',
                        # start_angle=0,
                        range_r=[0,5],
                        direction='clockwise')  # or counterclockwise
    fig.update_traces(fill='toself')
    st.write(fig)

def main():
    st.set_page_config(layout="centered", page_icon="🚗", page_title="YouTube Comment Analyzer")

    st.title("🚗 YouTube Comment Analyzer 📊")

    space(2)

    cars = ["Porsche_911_GT3__Porsche",
            "Porsche_911_Sport_Classic​__Porsche",
            "Porsche_911_GT3__Carfection",
            "Porsche_911_GT3__carwow",
            "Porsche_911_GT3_Touring__Collecting_Cars"
            ]
    source = merge_df(cars)
    all_models = source["car"].unique().tolist()
    models = st.multiselect("Choose models to visualize", all_models, all_models[:2])

    space(1)

    all_features = source["feature"].unique().tolist()
    features = st.multiselect("Choose features to visualize", all_features, all_features[:5])

    space(1)

    source = source[source["car"].isin(models)]
    source = source[source["feature"].isin(features)]
    radar_chart(source)

if __name__ == '__main__':
    main()