import plotly.express as px 
import csv
with open("c106/AverageTV.csv") as f:
    df= csv.DictReader(f)
    fig=px.scatter(df,x="Size",y="Time")
    fig.show()