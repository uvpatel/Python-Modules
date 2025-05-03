import streamlit as st
import pandas as pd

st.title("chai Sale Dashboard")

file = st.file_uploader("Upload your csv file",type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Priview")
    st.dataframe(df)

if file:
    st.subheader("Summary stats")
    st.write(df.describe())

if file:
    cities = df["City"].unique()
    selected_city = st.selectbox("Filter by cities",cities)
    filtered_data = df[df["City"] == selected_city ]
    st.dataframe(filtered_data)
    