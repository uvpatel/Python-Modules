import streamlit as st


st.title("Chai Poll")

col1,col2 = st.columns(2)


with col1:
    st.header("Masala Chai")
    # st.image("url",width=100)
    vote1 = st.button("vote Masala Chai")
with col2:
    st.header("Vote Adrak Chai")
    # st.image("url",width=100)
    vote2 = st.button("vote Adrak Chai")


if vote1:
    st.success("You Successfully Vote to Masal Chai")

elif vote2:
    st.success("You Successfully Vote to Adrak Chai")


name = st.sidebar.text_input("Enter your name")    
tea = st.sidebar.selectbox("Choose your chai",["Adrak chai","Kesar","Masala"])

st.write(f"Welcome {name} and your {tea} chai is getting ready. ")

with st.expander("show chai making instructions"):
    st.write("""
            1. Boil water with tea leaves.
            2. Add milk and spices
            3. Serve hot
""")
st.markdown('## Welcome to Chai App')

st.markdown('>Block Quote')