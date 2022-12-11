
#libraries
import streamlit as st
import pandas as pd
import plotly.express as px
st.header("Lung Cancer and Smoking")
st.write('Nowadays, a large number of people smoke cigarettes and tobacco in its various forms.It hearts their health and leads to a lot of diseases such as lung cancer and others.')
st.header('The purpose of the projec')
st.write('1)Show the relationship between the presence of lung cancer in people and their habit of smoking
2)Find is there a difference in the incidence of cancer in men and women when exposed to smoking')
data =pd.read_csv("survey_lung_cancer.csv")
data.dropna()

data.describe().loc[['mean', '50%', 'std']]

chart1 = px.histogram(data, x="AGE")
st.plotly_chart(chart1)

fig = px.pie(data, values='SMOKING', names='GENDER')
st.plotly_chart(fig)

fig = px.bar(data, x='LUNG_CANCER')
st.plotly_chart(fig)

fig = px.histogram(data, x="AGE",y='SMOKING', color="GENDER")
st.plotly_chart(fig)

fig = px.density_heatmap(data, x="AGE", y="LUNG_CANCER", facet_row="SMOKING", facet_col="GENDER")
st.plotly_chart(fig)

data = data.assign(lung_cancer__of_each_gender = data.GENDER + data.LUNG_CANCER)
# merging graphs

fig = px.bar(data, x='lung_cancer__of_each_gender',)
st.plotly_chart(fig)
