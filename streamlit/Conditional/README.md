# ☕ Chai Maker App using Streamlit

Welcome to the **Chai Maker App** – a fun and interactive Streamlit application that lets users brew their own virtual cup of chai!

---

## 🧠 What You Will Learn

- How to use Streamlit widgets like `button`, `checkbox`, `radio`, `selectbox`, `slider`, `number_input`, and `text_input`
- How to handle user inputs and provide instant feedback
- How to make your app interactive and fun

---

## 🚀 Getting Started

### 🔧 Prerequisites
- Python 3.7 or above
- pip
- Streamlit

Install Streamlit if not already installed:
```bash
pip install streamlit
```

---

## 🛠️ Run the App

```bash
streamlit run app.py
```

---

## 💻 App Features & Code Overview

```python
import streamlit as st

st.title("Chai Maker App")

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

cups = st.number_input("How many cups",min_value=1,max_value=10,step=1)
st.write(f"Selected sugar level {cups}")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Welcome, {name} ! Your chai is on the way")

dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth is {dob}")
```

---

## ✨ Features
- ☕ Simulates the chai-making process
- ✅ Optionally add masala
- 🧪 Choose chai base and flavour
- 🍬 Customize sugar level with slider
- 🔢 Set number of cups
- 🙋 Personalize with your name and DOB

---

## 📌 Future Add-ons
- Add image of chai cup based on choices
- Generate summary of your perfect chai recipe
- Add temperature and brewing time sliders

---

## 📞 Contact
Made with ❤️ by **Urvil**  
Email: [uvpatel7271@gmail.com](mailto:uvpatel7271@gmail.com)
