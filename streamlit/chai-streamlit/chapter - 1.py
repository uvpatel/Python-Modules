import streamlit as st

st.title("Hello chai app")
st.subheader("Brewed with streamlit")
st.text("welcome to you first interactive app")
st.write("Choose your fav. chai")

chai = st.selectbox("Your fav chai: ",["Masala chai","Lemon tea","adrak chai","kesar chai"])


st.write(f"Your choose {chai}. Excellent choice.")

st.success("Your chai has been brewed")