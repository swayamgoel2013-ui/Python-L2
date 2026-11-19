# TODO: write the code for your streamlit chatbot app here

import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(override=True) 
genai.configure(api_key="API_KEY")
API_KEY = os.getenv("API_KEY")

# set up the model, "gemini-2.5-flash" is a good model to start with
model = genai.GenerativeModel(model_name="gemini-2.5-flash")

# start a conversation
chat = model.start_chat(history=[])

# intro message
st.header("Welcome to the Gemini Chatbot!")

request = st.text_input("You: ")
response = chat.send_message(request).text

st.text_input(f"User:    {request}")
st.write(f"Chatbot: {response}")
# conversation loop
while (True):
    # user input
    st.write = input("Enter your prompt: ")
    # breaking condition
    if(request == "bye"):
        break
    # update chat
    response = chat.send_message(request).text
    st.text_input(f"\nYou >> {request}")
    st.write(f"\nBot >> {response}")

# closing message
st.write("\nGoodbye! Have a nice day!")

