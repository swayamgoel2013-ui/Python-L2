import streamlit as st
from PIL import Image

st.write("hello world")
st.title("this is a title")
st.code("what are ")
image = Image.open('Dog.avif')
st.image(image, caption = 'dog image')
