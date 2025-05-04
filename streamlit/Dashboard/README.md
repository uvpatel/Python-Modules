# 📊 **Simple Sales Dashboard**

Welcome to the **Simple Sales Dashboard** app! This app helps you visualize sales data and key metrics based on various filters.

---

## 🚀 **What You Will Learn**

- How to create a sales dashboard using Streamlit 📈
- How to filter data based on multiple criteria (region, product) 🔍
- How to visualize key performance indicators (KPIs) such as revenue and units sold 💰
- How to create bar and line charts with Streamlit 📊

---

## 🔧 **Requirements**

- Python 3.7 or higher
- pip
- Streamlit
- Pandas
- Numpy

#### **Install the required libraries:**
```bash
pip install streamlit pandas numpy
```

---

## ▶️ **Run the App**

```bash
streamlit run sales_dashboard.py
```

---

## 💡 **Code Overview**

```python
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Simple Sales Dashboard", layout="wide")

# Dummy Data
@st.cache_data
def load_data():
    np.random.seed(42)
    data = {
        "Date": pd.date_range("2024-01-01", periods=60),
        "Region": ["North", "South", "East", "West"] * 15,
        "Product": ["Chai", "Coffee", "Green Tea"] * 20,
        "Revenue": np.random.randint(500, 3000, 60),
        "Units_Sold": np.random.randint(20, 100, 60)
    }
    return pd.DataFrame(data)

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters 🔍")
region_filter = st.sidebar.multiselect("Select Region", df["Region"].unique(), default=df["Region"].unique())
product_filter = st.sidebar.multiselect("Select Product", df["Product"].unique(), default=df["Product"].unique())

# Filter Data
filtered_df = df[df["Region"].isin(region_filter) & df["Product"].isin(product_filter)]

# KPI Section
st.title("📈 Simple Sales Dashboard")

total_revenue = filtered_df["Revenue"].sum()
total_units = filtered_df["Units_Sold"].sum()
avg_units = filtered_df["Units_Sold"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue 💰", f"₹{total_revenue:,}")
col2.metric("Total Units Sold 📦", total_units)
col3.metric("Avg Units per Day 📅", f"{avg_units:.2f}")

st.markdown("---")

# Revenue by Product using built-in bar chart
st.subheader("Revenue by Product 📊")
revenue_chart = filtered_df.groupby("Product")["Revenue"].sum()
st.bar_chart(revenue_chart)

# Units Sold Over Time using line chart
st.subheader("Units Sold Over Time 📈")
units_time = filtered_df.groupby("Date")["Units_Sold"].sum()
st.line_chart(units_time)

st.markdown("---")

# Show Table
st.subheader("Raw Data 📋")
st.dataframe(filtered_df.sort_values(by="Date", ascending=False), use_container_width=True)
```

---

## 🛠 **Features**

- **Sidebar Filters:** Select regions and products to filter the data. 🔍
- **KPIs:** Display total revenue, total units sold, and average units sold per day. 💰📦
- **Charts:**
  - **Bar Chart:** Revenue by product. 📊
  - **Line Chart:** Units sold over time. 📈
- **Data Table:** View raw data based on selected filters. 📋

---

## 🧠 **Tip**

- Add more filters to make the app more customizable. 🛠
- The caching mechanism `@st.cache_data` is used to optimize performance. ⚡

---

## 📬 **Contact**

- Made with ❤️ by **Urvil**
- Email: [uvpatel7271@gmail.com](mailto:uvpatel7271@gmail.com)

---
