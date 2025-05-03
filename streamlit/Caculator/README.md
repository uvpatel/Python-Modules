# 📅 Age Calculator using Streamlit

Welcome to the **Streamlit Age Calculator** project! This is a simple and interactive web application that allows users to calculate their age based on their date of birth and the current date.

---

## 🧠 What You Will Learn

- How to use **Streamlit** to create a web application  
- How to take **date input** from users  
- How to perform basic **date arithmetic** in Python  
- How to display results interactively  

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have the following installed on your system:

- Python 3.7 or above  
- pip  
- Streamlit  

If not installed, use the following command:

```bash
pip install streamlit
```

---

## 🛠️ How to Run the App

1. **Clone or download** this repository:

```bash
git clone https://github.com/your-username/streamlit-age-calculator.git
cd streamlit-age-calculator
```

2. **Run the application:**

```bash
streamlit run app.py
```

3. The app will automatically open in your browser at `http://localhost:8501`.

---

## 💻 Code Walkthrough

Here is the main code of the application:

```python
import streamlit as st

st.title("Calculator")
st.subheader("This is your Calculator for calculating your age.")

dob = st.date_input("Enter your date of birth: ")
current_year = st.date_input("Enter Current year: ")

age = current_year - dob

st.write(f"You are {age} old!")
```

---

### ❗ Issues in the Code

Currently, the code tries to subtract two dates directly (`current_year - dob`), which gives a `timedelta` object, not a clear age in years.

---

### ✅ Fixing the Code

To calculate the age in **years**, update the code as follows:

```python
import streamlit as st
from datetime import date

st.title("📅 Age Calculator")
st.subheader("Find out how old you are today!")

dob = st.date_input("Enter your date of birth:")
today = st.date_input("Enter the current date:", date.today())

if today >= dob:
    age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.success(f"You are {age_years} years old! 🎉")
else:
    st.error("Error: Date of birth is after the current date!")
```

---

## ✨ Features

- 🎈 Simple and interactive UI  
- 📆 Accurate age calculation  
- 🧠 Error handling for incorrect date selection  
- 🔄 Real-time results without page reloads  

---

## 📌 Future Improvements

- Add support for age in months/days  
- Add theme switcher (light/dark)  
- Add birthday countdown  
- Deploy the app on **Streamlit Cloud**  

---

## 🌐 Deployment

To deploy your app online:

1. Push your code to GitHub.  
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).  
3. Connect your GitHub repository and deploy your app for free.

---

## 🙌 Contributing

Feel free to fork the repo and submit a pull request for:

- Bug fixes  
- Feature additions  
- UI improvements  

---

## 🧾 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 📞 Contact

Created with ❤️ by **Urvil**  
Have questions? Feel free to reach out via [email](mailto:uvpatel7271@gmail.com).
