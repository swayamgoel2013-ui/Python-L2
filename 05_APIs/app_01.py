import streamlit as st
import requests
import json

def get_exchange_rates(currency="INR"):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{currency}")
    return json.loads(response.text)

if "exchange_rates" not in st.session_state:
    st.session_state.exchange_rates = get_exchange_rates()

st.title("Currency Converter")

amount = st.number_input("Enter the amount:", min_value=0)
currencies = list(st.session_state.exchange_rates["rates"].keys())  
convert_from = st.selectbox("Select the currency to convert from:", currencies)
convert_to = st.selectbox("Select the currency to convert to:", currencies)
    
st.session_state.exchange_rates = get_exchange_rates(convert_from)
multiplier = st.session_state.exchange_rates["rates"][convert_to]
answer = amount * multiplier

st.success(f"{amount:.2f} {convert_from} => {answer:.2f} {convert_to}")
