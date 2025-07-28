import streamlit as st
import pandas as pd
from data_utils import clean_data
from visualization import show_visuals

st.title("Data Analysis Tool")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("🔍 Raw Data Preview")
    st.write(df.head())

    cleaned_df = clean_data(df)

    st.subheader("🧼 Cleaned Data")
    
    # Filter options
    city_options = ["All"] + sorted(cleaned_df["City_Tier"].dropna().unique().tolist())
    occupation_options = ["All"] + sorted(cleaned_df["Occupation"].dropna().unique().tolist())

    selected_city = st.selectbox("Filter by City_Tier", city_options)
    selected_occupation = st.selectbox("Filter by Occupation", occupation_options)

    filtered_df = cleaned_df.copy()

    if selected_city != "All":
        filtered_df = filtered_df[filtered_df["City_Tier"] == selected_city]
    if selected_occupation != "All":
        filtered_df = filtered_df[filtered_df["Occupation"] == selected_occupation]

    st.write(filtered_df.head())

    st.subheader("📈 Visualizations")
    show_visuals(filtered_df)
