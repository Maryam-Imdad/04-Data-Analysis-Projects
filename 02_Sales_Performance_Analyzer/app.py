import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Sales Analyzer - Maryam Imdad", layout="wide", page_icon="📊")
st.title("📊 Sales Performance Analyzer")
st.markdown("**By Maryam Imdad | BS Data Science - Gujranwala**")
st.markdown("---")

uploaded = st.sidebar.file_uploader("📁 Sales CSV Upload Karo", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
else:
    st.sidebar.info("Sample Data pe Dashboard chal raha hai")
    np.random.seed(42)
    products = ['Laptop','Mobile','Tablet','Headphones','Watch']
    regions = ['Gujranwala','Lahore','Karachi','Islamabad','Faisalabad']
    df = pd.DataFrame({
        'Product': np.random.choice(products, 200),
        'Region': np.random.choice(regions, 200),
        'Sales': np.random.randint(500, 5000, 200),
        'Profit': np.random.randint(50, 800, 200),
        'Date': pd.date_range('2024-01-01', periods=200)
    })

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Sales", f"${df['Sales'].sum():,}")
c2.metric("Total Profit", f"${df['Profit'].sum():,}")
c3.metric("Total Orders", len(df))
c4.metric("Avg Profit", f"${df['Profit'].mean():.0f}")

st.markdown("---")
col1,col2 = st.columns(2)
with col1:
    prod_sales = df.groupby('Product')['Sales'].sum().reset_index()
    st.plotly_chart(px.bar(prod_sales, x='Product', y='Sales', color='Product', title="Sales by Product"), use_container_width=True)
with col2:
    st.plotly_chart(px.pie(df, names='Region', values='Sales', title="Sales by Region", hole=0.4), use_container_width=True)

col3,col4 = st.columns(2)
with col3:
    df['Month'] = pd.to_datetime(df['Date']).dt.month_name()
    monthly = df.groupby('Month')['Sales'].sum().reset_index()
    st.plotly_chart(px.line(monthly, x='Month', y='Sales', markers=True, title="Monthly Sales Trend"), use_container_width=True)
with col4:
    st.plotly_chart(px.scatter(df, x='Sales', y='Profit', color='Product', size='Profit', title="Profit vs Sales"), use_container_width=True)

st.subheader("Raw Data")
st.dataframe(df, use_container_width=True)
st.download_button("📥 Sample CSV Download", df.to_csv(index=False), "sales_sample.csv")
st.markdown("---")
st.markdown("Made with ❤️ by **Maryam Imdad**")