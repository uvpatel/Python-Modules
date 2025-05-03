import streamlit as st

st.title("Chai Maker App")


# here button is widget

if st.button("Make chai"):
    st.success("Your chai is brewed")


add_masala = st.checkbox("add Masala")

if add_masala:
    st.write("Masala added to your chai.")

tea_type = st.radio("Pick your chai base: ",["Milk","Water","Honey"])

st.write(f"Selected base {tea_type}")

flavour = st.selectbox("Choose flavour: ",["Adrak ","Kesar"])

st.write(f"Selected flavour {flavour}")

sugar = st.slider("Sugar level",0,5,2)
st.write(f"Sugar level:{sugar} spoon ")

# o to 5 and 2 is defult

cups = st.number_input("How many cups",min_value=1,max_value=10,step=1)

st.write(f"Selected sugar level {cups}")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Welcome, {name} ! Your chai is on the way")


dob = st.date_input("Select your date of birth")    

st.write(f"Your date of birth is {dob}")