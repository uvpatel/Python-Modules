import streamlit as st

st.title("Programming language Peaker.")
st.subheader("Choose your favorite Programming Language.")
st.write("You have to choose language according to your intrest.")

choice = st.selectbox(f"Choose Your favorite Language: ",["Python","C","c++","javascript","Java"])


print(f"You choose {choice}. Excellent choice")

st.success(f"You succesfully choosed your favorite language {choice}")