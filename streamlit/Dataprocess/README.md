# 💸 **Live Currency Converter App**

### 🎯 **Objective:**
Create an intuitive **Streamlit** application that converts an amount in **INR** (Indian Rupees) to a selected currency (**USD**, **EUR**, **GBP**, **JPY**) using a live exchange rate API. The app features user input for the amount, a dropdown for currency selection, and displays the converted amount with a success or error message.

### 🔑 **Features:**
- **Amount Input:** Users enter an amount in INR.
- **Currency Selection:** Dropdown to choose the target currency (USD, EUR, GBP, JPY).
- **Live Conversion:** Fetches real-time exchange rates using an API.
- **Feedback:** Displays success or error messages based on API response.

### 🧑‍💻 **Code:**

```python
import streamlit as st
import requests

st.title("Live Currency Converter 💸")

amount = st.number_input("Enter the amount in INR 💰", min_value=1)

target_currency = st.selectbox("Convert to: 🌍", ["USD", "EUR", "GBP", "JPY"])

if st.button("Convert 🔄"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        converted = rate * amount
        st.success(f"{amount} INR = {converted:.2f} {target_currency} 🎉")
    else:
        st.error("Failed to fetch conversion rate. 😔")
```

---

### 🧑‍💻 **How It Works:**

**Title:**  
The `st.title()` function sets the app title to "Live Currency Converter 💸".

**Amount Input:**  
The `st.number_input()` function allows users to input an amount in INR, with a minimum value of 1.

**Currency Selection:**  
The `st.selectbox()` function provides a dropdown menu to select the target currency (USD, EUR, GBP, JPY).

**Conversion Button:**  
The `st.button()` function triggers the conversion process when clicked.

**API Request:**  
The `requests.get()` function fetches live exchange rates from the `exchangerate-api.com` API using INR as the base currency.

**Feedback:**  
- If the API request is successful (`status_code == 200`), the app extracts the exchange rate, calculates the converted amount, and displays it using `st.success()`.
- If the request fails, an error message is shown using `st.error()`.

---

### 🚀 **Run the App:**

To run this Streamlit app, follow these steps:

1. **Save the Code:**  
   Save the Python code above in a file named `main.py`.

2. **Install Dependencies (if not installed):**  
   If you haven't installed Streamlit and Requests yet, open a terminal and type:

   ```bash
   pip install streamlit requests
   ```

3. **Run the App:**  
   Open a terminal, navigate to the folder where `currency_converter.py` is saved, and run:

   ```bash
   streamlit run main.py
   ```

   The app will automatically open in your default web browser!

4. **Enjoy!**  
   Enter an amount, select a currency, and click "Convert" to see the live conversion result! 🌟

---

### ✨ **Customization Ideas:**
- Add more currencies to the dropdown for broader conversion options. 🌐
- Include a reverse conversion feature (e.g., from USD to INR). 🔄
- Display a historical exchange rate chart using a plotting library like Matplotlib. 📊

---

### 💬 **Want to Learn More?**
Explore more Streamlit projects or dive into APIs for real-time data! Check out other assignments in this repo for inspiration. 👩‍💻👨‍💻

Feel free to star ⭐ the repo if you love it or contribute your own currency-related projects! 🚀
