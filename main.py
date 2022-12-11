#libraries
import pandas as pd
import plotly.express as px

data =pd.read_csv("survey_lung_cancer.csv")
data.dropna()

data.describe().loc[['mean', '50%', 'std']]

chart1 = px.histogram(data, x="AGE")
chart1.show()

fig = px.pie(data, values='SMOKING', names='GENDER')
fig.show()

fig = px.bar(data, x='LUNG_CANCER')
fig.show()

fig = px.histogram(data, x="AGE",y='SMOKING', color="GENDER")
fig.show()

fig = px.density_heatmap(data, x="AGE", y="LUNG_CANCER", facet_row="SMOKING", facet_col="GENDER")
fig.show()

data = data.assign(lung_cancer__of_each_gender = data.GENDER + data.LUNG_CANCER)
# merging graphs

fig = px.bar(data, x='lung_cancer__of_each_gender',)
fig.show()