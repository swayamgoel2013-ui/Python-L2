import streamlit as st
import time

st.write("main section of the app")
name = st.sidebar.text_input("Enter your name")

col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")

with col2:
    st.header("Column 2")

tabs = st.tabs(["Home", "About", "Contact"])

with tabs[0]:
    st.header("Home")
    st.write("Hello this is the homepage of my website")

with tabs[1]:
    st.header("About")
    st.write("This is the about page of my website")

with tabs[2]:
    st.header("Contact")
    st.write("This is the contact page of my website ")

with st.spinner("Wait for it"):
    time.sleep(5)
st.success("Done!")

st.write("Main section of the app")

st.warning("This is a warning message")
st.success("This is a success message")