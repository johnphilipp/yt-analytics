from utils import app
import streamlit as st

#-----------------------------------------------------------------------

st.set_page_config(layout="centered", page_icon="🚗", page_title="YouTube Comment Analyzer")

st.title("🚗 YouTube Comment Analyzer 📊")

app.space(2)

cars = ["Porsche_911_GT3__Porsche",
        "Porsche_911_Sport_Classic​__Porsche",
        "Bugatti_Centodieci__Bugatti"]
source = app.merge_df(cars)
all_models = source["car"].unique().tolist()
models = st.multiselect("Choose models to visualize", all_models, all_models[:2])

app.space(1)

all_features = source["feature"].unique().tolist()
features = st.multiselect("Choose features to visualize", all_features, all_features[:5])

app.space(1)

source = source[source["car"].isin(models)]
source = source[source["feature"].isin(features)]
app.radar_chart(source)