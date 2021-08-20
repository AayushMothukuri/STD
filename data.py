import pandas as pd
import plotly_express as px
df=pd.read_csv("data.csv")
fig=px.line(df,x="Country",y="InternetUsers")
fig.show()