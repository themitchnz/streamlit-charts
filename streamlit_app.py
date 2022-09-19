import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from bokeh.plotting import figure

st.set_page_config(
    page_title="NZDF Totara Charts", page_icon="⬇", layout="wide"
)

#Load CSV into a dataframe
csv = pd.read_csv('count.csv')
df = pd.DataFrame(csv)

#get highest total
max = int(df['Total'].max())

#setup Filters on sidebar


st.sidebar.subheader("Totara completion stats")
total_slider = st.sidebar.slider('Total Enrolments',0,max,(0,max)) #min, max, range select, steps

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    max = int(df['Total'].max())

#filter CSV from filters
filtered_dataframe = df[
    (df['Total'] > total_slider[0]) & (df['Total'] < total_slider[1])
    ]

st.line_chart(filtered_dataframe,x=csv.columns[0],y=['# Complete','# Not complete'],width=800,height=800)



#c = alt.Chart(csv).mark_line().encode(
   # x=csv.columns[0], y=csv.columns[1])
#st.altair_chart(c, use_container_width=True)

#p = figure(x_range=filtered_dataframe['Course Name'],title="Multiple line example", x_axis_label='x', y_axis_label='y')

#p.line(csv.columns[0], csv.columns[1], legend_label='Trend', line_width=2)
#p.line(filtered_dataframe['Course Name'], filtered_dataframe['# Complete'], legend_label="Temp.", color="green", line_width=2)
#p.line(filtered_dataframe['Course Name'], filtered_dataframe['# Not complete'], legend_label="Temp.", color="red", line_width=2)

#st.bokeh_chart(p, use_container_width=True)
