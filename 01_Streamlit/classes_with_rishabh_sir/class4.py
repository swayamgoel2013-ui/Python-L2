import streamlit as st

st.title("Word Counter Tool")

text = st.text_area("Enter your text", height=100)

word_count = len(text.split())
character_count = len(text)

st.write(f"Amount of words = {word_count}")

st.write(f"Amount of Characters = {character_count}")

