
# 📘 Assignment 1: **Programming Language Picker**

### 🎯 **Objective:**
Create a simple **Streamlit** application that lets users select their favorite programming language from a dropdown menu and displays a confirmation message.

### 🔑 **Features:**
- **Title:** "Programming Language Picker"
- **Subtitle:** "Choose your favorite Programming Language."
- **Instruction:** "You have to choose a language according to your interest."
- **Dropdown Menu:** A selectbox widget with options: Python, C, C++, JavaScript, and Java.
- **Output:** Displays a success message confirming the user's selection.

### 🧑‍💻 **Code:**

```python
import streamlit as st

# Title and instructions
st.title("Programming Language Picker")
st.subheader("Choose your favorite Programming Language.")
st.write("You have to choose a language according to your interest.")

# Dropdown menu for language selection
choice = st.selectbox("Choose Your favorite Language:", ["Python", "C", "C++", "JavaScript", "Java"])

# Display the user's choice
st.success(f"You successfully chose your favorite language: {choice}")
```

### 🛠️ **How It Works:**

1. **Title and Subtitle:**  
   The `st.title()` and `st.subheader()` functions set the main title and subtitle of your app.
   
   - 📝 **`st.title("Programming Language Picker")`** sets the main heading of the app.
   - 📜 **`st.subheader("Choose your favorite Programming Language.")`** gives a smaller subtitle for the task.
   
2. **Instructions:**  
   The `st.write()` function displays additional instructions to help the user understand what to do.
   
   - 📌 **`st.write("You have to choose a language according to your interest.")`** guides the user in a friendly tone.

3. **Dropdown Menu:**  
   The `st.selectbox()` function is used to create a dropdown menu with the options "Python," "C," "C++," "JavaScript," and "Java."

   - 🎯 **`st.selectbox("Choose Your favorite Language:", ["Python", "C", "C++", "JavaScript", "Java"])`** lets users select a language from the list.

4. **User Feedback:**  
   Once the user makes a selection, the `st.success()` function displays a success message with their choice.
   
   - ✅ **`st.success(f"You successfully chose your favorite language: {choice}")`** confirms the user's choice.

### 🚀 **Run the App:**

To run this Streamlit app, follow these steps:

1. **Save the Code:**  
   Save the Python code above in a file named `app.py`.

2. **Install Streamlit (if not installed):**  
   If you haven't installed Streamlit yet, open a terminal and type:
   ```bash
   pip install streamlit
   ```

3. **Run the App:**
   - Open a terminal, navigate to the folder where `app.py` is saved, and run:
     ```bash
     streamlit run app.py
     ```
   - The app will automatically open in your default web browser!

4. **Enjoy!**  
   You’ll see the app running and ready to use, allowing users to pick their favorite programming language and getting a success message.

---

### ✨ **Customization Ideas:**

- Add more languages or even additional instructions.
- Customize the layout and colors using Streamlit’s built-in features.
- Add more interactive widgets like buttons, sliders, or text input.

---

### 💬 **Want to Learn More?**

If you want to dive deeper into **Streamlit** or get more hands-on projects, check out the other assignments in this repo! 👩‍💻👨‍💻

Feel free to **star ⭐** the repo if you like it or contribute your own projects! 🚀
