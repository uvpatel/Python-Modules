# Chai Poll App

Welcome to the **Chai Poll** app, a fun way to vote for your favorite chai and interact with the app! Choose your favorite chai and get a personalized experience.

---

## 🚀 What You Will Learn

- How to use Streamlit for creating polls
- How to display success feedback based on user interactions
- How to use sidebar widgets for personalization

---

## 🔧 Requirements

- Python 3.7 or higher
- pip
- Streamlit

Install Streamlit:
```bash
pip install streamlit
```

## ▶️ Run the App
``` bash
Copy code
streamlit run chai_poll_app.py
```

💡 Code Overview

```python

import streamlit as st
```
### Python Code

```python code
st.title("Chai Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    vote1 = st.button("vote Masala Chai")
with col2:
    st.header("Vote Adrak Chai")
    vote2 = st.button("vote Adrak Chai")

if vote1:
    st.success("You Successfully Vote to Masala Chai")
elif vote2:
    st.success("You Successfully Vote to Adrak Chai")

name = st.sidebar.text_input("Enter your name")    
tea = st.sidebar.selectbox("Choose your chai",["Adrak chai","Kesar","Masala"])

st.write(f"Welcome {name} and your {tea} chai is getting ready.")

with st.expander("show chai making instructions"):
    st.write("""
            1. Boil water with tea leaves.
            2. Add milk and spices
            3. Serve hot
""")

st.markdown('## Welcome to Chai App')
st.markdown('>Block Quote')
```

---
## 🛠 Features
Vote for your favorite chai: Masala Chai or Adrak Chai

Sidebar personalization: Enter your name and select your preferred chai

Chai making instructions: Expandable section with chai-making steps

---

## 🧠 Tip
You can easily enhance the app by adding images for each chai type.

---
## 📬 Contact
- Made with ❤️ by **Urvil**
- Email: [uvpatel7271@gmail.com](mailto:uvpatel7271@gmail.com)
---
