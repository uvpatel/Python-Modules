import streamlit as st

st.title("Calculator")
st.subheader("This is your Calculator for calculating your age.")

dob = st.date_input("Enter your date of birth: ")
current_year = st.date_input("Enter Current year: ")

age = current_year - dob

st.write(f"You are {age} old!")