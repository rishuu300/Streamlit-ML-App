import streamlit as st # type: ignore
import pandas as pd
import numpy as np

# Tile
st.title("Streamlit Text Input")

# Name
name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}")
   
# Age 
age = st.slider("Select your age", 0, 100, 25)

st.write(f"Your age is {age}")

# Options
options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")

# DataFrame
data = {
"Name": [ "John", "Jane", "Jake", "Jill"],
"Age" : [28, 24, 35, 40],
"City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
st.write(df)

# Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)