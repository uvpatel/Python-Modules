# 🍵 **Chai Poll App**

### 🎯 **Objective:**
Create a fun **Streamlit** application that lets users vote for their favorite chai: **Masala Chai** or **Adrak Chai**. The app also provides an option for the user to input their name and choose their preferred chai from a sidebar. Additionally, the app displays a simple chai-making recipe.

### 🔑 **Features:**
- **Voting:** Two options for voting: Masala Chai and Adrak Chai.
- **User Feedback:** Displays a success message when a vote is cast.
- **Sidebar Input:** Users can input their name and choose a chai.
- **Chai-Making Instructions:** Expandable section showing how to make chai.

### 🧑‍💻 **Code:**

```python
import streamlit as st

st.title("Chai Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    vote1 = st.button("Vote Masala Chai")
    
with col2:
    st.header("Adrak Chai")
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("You Successfully Voted for Masala Chai")
elif vote2:
    st.success("You Successfully Voted for Adrak Chai")

name = st.sidebar.text_input("Enter your name")    
tea = st.sidebar.selectbox("Choose your chai", ["Adrak Chai", "Kesar", "Masala"])

st.write(f"Welcome {name}, and your {tea} chai is getting ready.")

with st.expander("Show Chai Making Instructions"):
    st.write("""
            1. Boil water with tea leaves.
            2. Add milk and spices.
            3. Serve hot.
    """)

st.markdown('## Welcome to Chai App')
st.markdown('> Block Quote')
```

---

### 🧑‍💻 **How It Works:**

**Title:**  
The `st.title()` function sets the title of the app to "Chai Poll".

**Columns for Voting Options:**  
The `st.columns(2)` function divides the app into two columns for Masala Chai and Adrak Chai voting options.

**Voting Buttons:**  
The `st.button()` function creates two buttons allowing users to vote for Masala Chai or Adrak Chai.

**Feedback:**  
Once a vote is cast, the `st.success()` function displays a success message confirming the user's vote.

**Sidebar Input:**  
The sidebar (`st.sidebar`) allows users to input their name and select their favorite chai using a dropdown (`st.selectbox`).

**Chai-Making Instructions:**  
The `st.expander()` creates an expandable section that shows the instructions for making chai when clicked.

**Markdown Content:**  
The `st.markdown()` function is used to display headings and quotes in markdown format.

---

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
   Open a terminal, navigate to the folder where `app.py` is saved, and run:

   ```bash
   streamlit run app.py
   ```

   The app will automatically open in your default web browser!

4. **Enjoy!**  
   You’ll see the app running with voting options for your favorite chai and an interactive sidebar to input your details!

---

### ✨ **Customization Ideas:**
- Add images of chai cups or brewing process for more visual appeal.
- Customize the instructions for different types of chai or tea varieties.
- Enhance the voting system to allow multiple votes or show results.

---

### 💬 **Want to Learn More?**
If you want to explore more projects like this or dive deeper into Streamlit, check out the other assignments in this repo! 👩‍💻👨‍💻

Feel free to star ⭐ the repo if you like it or contribute your own chai-related projects! 🚀
