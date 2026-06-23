import streamlit as st
import pandas as pd

# Title
st.title("Nigeria Incidents Analysis NG")

# Introduction
st.write("This app provides an overview of incidents, accidents, and violence in Nigeria.")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read data
    df = pd.read_csv(uploaded_file)

    # Display first rows
    st.subheader("Dataset Overview")
    st.write(df.head())

    # Show basic information
    st.subheader("Data Summary")
    st.write(df.describe())

    # Show number of rows and columns
    st.subheader("Dataset Shape")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

else:
    st.info("Please upload the Nigeria incidents CSV dataset to begin analysis.")
