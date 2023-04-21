import csv
import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv("data.csv")

fig=go.Figure(go.Scatter(
    x=df.groupby("Level")["Attempt"].mean(),
    y=["Level1","Level2","Level3","Level4"],
    orientation='h'))

fig.show()