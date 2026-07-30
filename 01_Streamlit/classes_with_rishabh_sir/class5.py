import streamlit as st

with st.form("My form"):
    name = st.text_input("Enter ur name")
    age = st.number_input("Enter ur age", min_value=0, max_value=100)
    hobbies = st.multiselect("Choose your hobbies", ['sports', 'coding', 'art', 'music', 'dance', 'sleeping'])
    sumbit = st.form_submit_button("Sumbit your form")

if sumbit:
    st.write("Thank you for filling the form")