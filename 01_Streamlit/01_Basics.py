# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st

# Headings
st.title("This is a Title")  # Largest heading
st.header("This is a Header")  # Secondary heading
st.subheader("This is a Subheader")  # Tertiary heading

# Plain Texts
st.text("st.text: Some text") # to display plain text
st.write("st.write: Some text") # more versatile than text, can handle (dataframes, markdowns, etc.)

# Formatted Texts
st.caption("st.caption: This is a caption.")
st.markdown("st.markdown: **Bold text**, *italic text*, and click on the [link](https://www.google.com).")
st.latex(r"st.latex: a^2 + b^2 = c^2")

# Coding Texts
st.code("""
def hello_world():
    print("Hello, World!")
""", language="python")
data = {"count": 3, "students": [{"Alice":11, "Bob":12, "Charlie":13}]}
st.json(data)

# Special Messages
st.success("This is a success message!")
st.error("This is an error message.")
st.warning("This is a warning.")
st.info("This is an informational message.")

# Expander
with st.expander("Expand for more details"):
    st.write("Here is some detailed information.")

# Text input
name = st.text_input("Enter your name")

# Number input
age = st.number_input("Enter your age", min_value=0, max_value=120, value=20)

# Button
click = st.button("Click Me")
if (click):
    st.write(f"Hello, {name}! You are {age} years old.")
else:
    st.write("Click the button to see something happen.")

# Slider
value = st.slider("Select a value", min_value=0, max_value=100, value=50)
st.write(f"{value = }")

# Select slider
level = st.select_slider("Choose a level", options=["Low", "Medium", "High"], value="Medium")
st.write(f"{level = }")

# Checkbox
check = st.checkbox("Show Text")
st.write("f{check = }")

# Radio
choice = st.radio("Pick one:", ["A", "B", "C"])
st.write(f"{choice = }")

# Selectbox
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"{option = }")

# CheckGroup
selected = []
option1 = st.checkbox("Option 1")
if option1:
    selected.append("Option 1")
option2 = st.checkbox("Option 2")
if option2:
    selected.append("Option 2")
option3 = st.checkbox("Option 3")
if option3:
    selected.append("Option 3")
st.write(f"{selected = }")

# Multiselect
options = st.multiselect("Choose multiple options", ["Option 1", "Option 2", "Option 3"])
st.write(f"{options = }")

# Date
date = st.date_input("Pick a date")
st.write(f"{date = }")

# File uploader
uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv", "json"])
if uploaded_file is not None:
    st.write("Uploaded file name:", uploaded_file.name)
