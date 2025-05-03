# ☕ Hello Chai App using Streamlit

Welcome to the **Hello Chai App** – your very first interactive chai experience using Streamlit!

---

## 🎯 What You'll Learn

- Using Streamlit to build simple and fun web apps
- Implementing headers and text content
- Creating interactive dropdowns (`selectbox`)
- Displaying user selections and success messages

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.7 or later
- pip
- Streamlit

Install Streamlit:
```bash
pip install streamlit
```

### ▶️ Run the App
```bash
streamlit run hello_chai_app.py
```

---

## 💻 Code Overview

```python
import streamlit as st

st.title("Hello chai app")
st.subheader("Brewed with streamlit")
st.text("welcome to you first interactive app")
st.write("Choose your fav. chai")

chai = st.selectbox("Your fav chai: ",["Masala chai","Lemon tea","adrak chai","kesar chai"])
st.write(f"Your choose {chai}. Excellent choice.")

st.success("Your chai has been brewed")
```

---

## 🧾 App Features
- Display a title, subheader, and custom message
- Allow the user to select their favorite type of chai
- Show feedback message based on user input
- Display a success message once chai is brewed

---

## 🧠 Learning Outcome
- Great starting point to learn Streamlit UI elements
- Quick practice for interactive Python web apps

---

## 📬 Contact
Made with ❤️ by **Urvil**  
Email: [uvpatel7271@gmail.com](mailto:uvpatel7271@gmail.com)
