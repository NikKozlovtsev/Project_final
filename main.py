
#libraries
import streamlit as st
import pandas as pd
import plotly.express as px
st.header("Lung Cancer and Smoking")
st.write('Nowadays, a large number of people smoke cigarettes and tobacco in its various forms.It hearts their health and leads to a lot of diseases such as lung cancer and others.')
st.subheader('The purpose of the project')
st.write('Show the relationship between the presence of lung cancer in people and their habit of smoking.')
st.write('Find is there a difference in the incidence of cancer in men and women when exposed to smoking.')
st.subheader('Hypothesis')
st.write('Men and women have the same resistance to nicotine and suffer from lung cancer approximately equally.')
st.subheader('Dataset and its midean, mean and std')
data =pd.read_csv("survey_lung_cancer.csv")
data.dropna()

data.describe().loc[['mean', '50%', 'std']]
st.subheader("The all ages of respondents")

chart1 = px.histogram(data, x="AGE")
st.plotly_chart(chart1)
st.write("This statistics show that the overwhelming majority  that took part in this survey were in the range of 40 to 80 years. So, our research will give information about elderly people.")
st.subheader("GENDERS of respondents")
fig = px.pie(data, values='SMOKING', names='GENDER')
st.plotly_chart(fig)
st.write("It can be seen that differnce between male and female respondents is pretty equel to each other, which means that the data obtained during our project will be more reliable.")
st.subheader("The presence of lung cancer in respondents")
fig = px.bar(data, x='LUNG_CANCER')
st.plotly_chart(fig)
st.write("The statistics show us that over 80% of respondets have lung cancer that means that these problem is not rare one and understanding of the factors that lead to lung cancer will help people to prevent this disease.")


fig = px.histogram(data, x="AGE",y='SMOKING', color="GENDER")
st.plotly_chart(fig)

fig = px.density_heatmap(data, x="AGE", y="LUNG_CANCER", facet_row="SMOKING", facet_col="GENDER")
st.plotly_chart(fig)

data = data.assign(lung_cancer__of_each_gender = data.GENDER + data.LUNG_CANCER)
# merging graphs

fig = px.bar(data, x='lung_cancer__of_each_gender',)
st.plotly_chart(fig)
