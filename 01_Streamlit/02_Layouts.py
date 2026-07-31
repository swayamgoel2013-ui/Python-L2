# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st
import random as rn


# Sidebar
st.sidebar.title("Sidebar Title")
st.sidebar.header("Sidebar")
choice = st.sidebar.radio("Select a view:", ["Home", "About", "Contact"])
st.title(f"This is the {choice} page!")


# Columns
st.header("Columns")
col1, col2 = st.columns([1, 2])  # col2 is twice as wide as col1
with col1:
    st.write("This is the first column")
    st.write("We can use it as the input section")
    passwordSize = st.slider("Pick Password Size", 4, 20)
with col2:
    st.write("This is the second column")
    st.write("We can use it as the output section")
    password = ""
    for i in range(passwordSize):
        x = rn.randint(0, 25)
        password += chr(ord('A') + x)
    st.write(f"You password: {password}")


# Tabs
st.header("Tabs")
tab1, tab2, tab3 = st.tabs(["Chart", "Data", "Info"])
with tab1:
    st.write("Chart view")
with tab2:
    st.write("Data view")
with tab3:
    st.write("Information view")


# Tables
st.header("Tables")
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 22],
    "Marks1": [67, 78, 89],
    "Marks2": [67, 78, 89],
    "Marks3": [67, 78, 89],
    "Marks4": [67, 78, 89],
    "Marks5": [67, 78, 89],
    "Marks6": [67, 78, 89],
    "Marks7": [67, 78, 89],
    "Marks8": [67, 78, 89],
    "Marks9": [67, 78, 89],
    "Marks10": [67, 78, 89],
    "Marks11": [67, 78, 89],
    "Marks12": [67, 78, 89],
}
st.header("Static Table (using st.table)")
st.table(data)
