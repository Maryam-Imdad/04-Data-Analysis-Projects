import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Customer EDA - Maryam Imdad", layout="wide", page_icon="🔍")
st.title("🔍 Customer EDA Dashboard")
st.markdown("**By Maryam Imdad | BS Data Science - Gujranwala**")
st.markdown("---")

# Sidebar
uploaded = st.sidebar.file_uploader("📁 Customer CSV Upload Karo", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
else:
    st.sidebar.info("Sample Data pe Dashboard chal raha hai")
    np.random.seed(42)
    df = pd.DataFrame({
        'Age': np.random.randint(18, 65, 200),
        'Gender': np.random.choice(['Male','Female'], 200),
        'Region': np.random.choice(['Gujranwala','Lahore','Karachi','Islamabad','Faisalabad'], 200),
        'Spending': np.random.randint(200, 5000, 200),
        'Rating': np.random.randint(1, 6, 200),
        'Purchase_Frequency': np.random.randint(1, 20, 200)
    })

# Metrics
c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Customers", len(df))
c2.metric("Avg Age", f"{df['Age'].mean():.0f}")
c3.metric("Avg Spending", f"${df['Spending'].mean():.0f}")
c4.metric("Avg Rating", f"{df['Rating'].mean():.1f} ⭐")

st.markdown("---")
col1,col2 = st.columns(2)
with col1:
    st.subheader("Missing Values")
    st.bar_chart(df.isnull().sum())
    st.subheader("Age Distribution")
    st.plotly_chart(px.histogram(df, x='Age', color='Gender', title="Age by Gender"), use_container_width=True)

with col2:
    st.subheader("Region Distribution")
    st.plotly_chart(px.pie(df, names='Region', values='Spending', title="Spending by Region", hole=0.4), use_container_width=True)
    st.subheader("Spending vs Age")
    st.plotly_chart(px.scatter(df, x='Age', y='Spending', color='Gender', size='Rating', title="Age vs Spending"), use_container_width=True)

st.subheader("Correlation Heatmap")
numeric_df = df.select_dtypes(include='number')
st.plotly_chart(px.imshow(numeric_df.corr(), text_auto=True, title="Correlation Matrix"), use_container_width=True)

st.subheader("Raw Data")
st.dataframe(df.head(20), use_container_width=True)
st.download_button("📥 Sample CSV Download", df.to_csv(index=False), "customer_sample.csv")
st.markdown("---")
st.markdown("Made with ❤️ by **Maryam Imdad**")