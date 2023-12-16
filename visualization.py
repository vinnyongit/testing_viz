import pandas as pd
import plotly.express as px

csv_url = "https://github.com/marestaing/hosting/blob/main/visited_states.csv?raw=true"
df = pd.read_csv(csv_url)


fig = px.choropleth(
    df,
    locations="State",  
    locationmode="USA-states",
    color="Count", 
    scope="usa",
    color_continuous_scale="Viridis",  
    title="States Visited by APCSP Students",
    labels={"Count": "Number of Students"}
)


fig.show()
