# ☕ **Chai Sale Dashboard**

### 🎯 **Objective:**
Create a **Streamlit** application that allows users to upload a CSV file containing chai sales data, preview the data, view summary statistics, and filter the data by city.

### 🔑 **Features:**
- **File Upload:** Users can upload a CSV file with sales data. 📂
- **Data Preview:** Displays the uploaded dataset in a table. 📋
- **Summary Statistics:** Shows basic statistical metrics of the dataset. 📊
- **City Filter:** Allows filtering of data by selecting a city from a dropdown. 🌆

### 🧑‍💻 **Code:**

```python
import streamlit as st
import pandas as pd

st.title("Chai Sale Dashboard ☕")

file = st.file_uploader("Upload your CSV file 📂", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview 📋")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats 📊")
    st.write(df.describe())

if file:
    cities = df["City"].unique()
    selected_city = st.selectbox("Filter by Cities 🌆", cities)
    filtered_data = df[df["City"] == selected_city]
    st.dataframe(filtered_data)
```

---

### 🧑‍💻 **How It Works:**

**Title:**  
The `st.title()` function sets the app title to "Chai Sale Dashboard ☕".

**File Upload:**  
The `st.file_uploader()` function allows users to upload a CSV file, restricted to `.csv` format.

**Data Preview:**  
If a file is uploaded, `pd.read_csv()` reads the file into a Pandas DataFrame, and `st.dataframe()` displays the data as a table.

**Summary Statistics:**  
The `df.describe()` function generates summary statistics (e.g., mean, min, max) for numerical columns, displayed using `st.write()`.

**City Filter:**  
The `st.selectbox()` function creates a dropdown with unique city names from the "City" column. The DataFrame is filtered to show only rows matching the selected city, displayed using `st.dataframe()`.

---

### 🚀 **Run the App:**

To run this Streamlit app, follow these steps:

1. **Save the Code:**  
   Save the Python code above in a file named `chai_sale_dashboard.py`.

2. **Install Dependencies (if not installed):**  
   If you haven't installed Streamlit and Pandas yet, open a terminal and type:

   ```bash
   pip install streamlit pandas
   ```

3. **Run the App:**  
   Open a terminal, navigate to the folder where `chai_sale_dashboard.py` is saved, and run:

   ```bash
   streamlit run chai_sale_dashboard.py
   ```

   The app will automatically open in your default web browser!

4. **Enjoy!**  
   Upload a CSV file, preview the data, view summary stats, and filter by city! 🌟

---

### ✨ **Customization Ideas:**
- Add more filters (e.g., by date or product) for enhanced data exploration. 🔍
- Include visualizations like bar or line charts to show sales trends. 📈
- Add error handling for invalid CSV files or missing "City" columns. ⚠️

---

### 💬 **Want to Learn More?**
Explore more Streamlit projects or dive into data visualization techniques! Check out other assignments in this repo for inspiration. 👩‍💻👨‍💻

Feel free to star ⭐ the repo if you love it or contribute your own chai-related projects! 🚀
