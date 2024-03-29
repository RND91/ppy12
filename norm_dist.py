import pandas as pd 
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Avg Rating"]],["Average Rating"],show_hist=True)
fig.show()