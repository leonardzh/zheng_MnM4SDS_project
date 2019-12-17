# -*- coding: utf-8 -*-
# Copyright 2018-2019 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An example of showing geographic data."""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import os
cwd = os.getcwd()

DATE_TIME = "date/time"
DATA_URL = (
    "hour_si_deckgl.csv"
)


st.title('NYC Taxi Data')
st.markdown(
"""
This is a demo of a Streamlit app that shows the Uber pickups
geographical distribution in New York City. Use the slider
to pick a specific hour and look at how the charts change.

[See source code](./streamlitdemo.py)
""")

#@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    return data


data = load_data(100000)
flowColors = [

  [12, 44, 132],
#   [34, 94, 168],
  [29, 145, 192],
#   [65, 182, 196],
  [127, 205, 187],
#   [199, 233, 180],
  [255, 255, 204],
#   [255, 255, 178],
  [254, 217, 118],
#   [254, 178, 76],
  [253, 141, 60],
#  [252, 78, 42],
  [227, 26, 28],
  [177, 0, 38]
]

hour = st.slider("Hour to look at", 0, 23)
trip_thres = st.slider("Minimum trips (square) to look at", 1, 30)
data = data[data.hour == hour]
color_cat = pd.qcut(data['count'],8,duplicates= 'drop')
data = data[data['count'] >= trip_thres*trip_thres]


data['color_idx'] = color_cat.cat.codes

data['colorR'] = data['color_idx'].apply(lambda x: flowColors[x][0])
data['colorG'] = data['color_idx'].apply(lambda x: flowColors[x][1])
data['colorB'] = data['color_idx'].apply(lambda x: flowColors[x][2])
data['targetColorR'] =data['colorR']
data['targetColorG'] =data['colorG']
data['targetColorB'] =data['colorB']
# df = rand_data()
# df2 = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [40.78, -73.97],
#     columns=['lat', 'lon'])
st.subheader("Geo data between %i:00 and %i:00" % (hour, (hour + 1) % 24))
# midpoint = (np.average(data["lat"]), np.average(data["lon"]))
st.deck_gl_chart(
    viewport={
        "latitude": 40.78, 
        "longitude": -73.97,
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        {
            "type": "ArcLayer",
            "data": data,
            "encoding":{
                "getColorR": flowColors[0][0],
            "getColorG":flowColors[0][1],
            "getColorB":flowColors[0][2],
            "getTargetColorR": flowColors[0][0],
            "getTargetColorG":flowColors[0][1],
            "getTargetColorB":flowColors[0][2],
                "getLatitude":{"field":"lat"},
                "getLongitude":{"field":"lon"},
                "getTargetLatitude":{"field":"lat2"},
                "getTargetLongitude":{"field":"lon2"},
            
            },
            
            # "radius": 100,
            # "elevationScale": 4,
            # "elevationRange": [0, 1000],
            # "pickable": True,
            # "extruded": True,
        }
    ],
)


# st.subheader("Breakdown by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24))
# filtered = data[
#     (data[DATE_TIME].dt.hour >= hour) & (data[DATE_TIME].dt.hour < (hour + 1))
# ]
# hist = np.histogram(filtered[DATE_TIME].dt.minute, bins=60, range=(0, 60))[0]
# chart_data = pd.DataFrame({"minute": range(60), "pickups": hist})
# st.write(alt.Chart(chart_data, height=150)
#     .mark_area(
#         interpolate='step-after',
#         line=True
#     ).encode(
#         x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
#         y=alt.Y("pickups:Q"),
#         tooltip=['minute', 'pickups']
#     ))

if st.checkbox("Show raw data", False):
    st.subheader("Raw data by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24))
    st.write(data)
