import streamlit as st

if st.button("click me"):
    st.write("button is clicked")



check1= st.checkbox("bmw")
check2= st.checkbox("mercedes")
check3= st.checkbox("lamborgini")


contries = st.selectbox("choose a country", ['india', 'usa', 'china', 'russia'])
st.write(f"you have selected {contries}")

colors = st.multiselect("choose a color", ['red','blue', 'green', 'yellow' ])

age = st.slider("age", min_value=0, max_value=100)
st.write(f"your age is {age}")

name = st.text_input("enter your name")
st.write(f"your name is {name}")

review = st.text_area("write a review", height=100)
st.write("Thank you for your review")

file = st.file_uploader("choose file", type = ["jpeg", "png"])

color = st.color_picker("pick a color", "#000000")
