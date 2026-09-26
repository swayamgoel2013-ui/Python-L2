import streamlit as st
import requests

st.title("Currency Converter")

currencies = {
    "USD": "US Dollar",
    "INR": "Indian Rupee",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan"
}

# Sidebar
st.sidebar.title("Settings")

amount = st.sidebar.number_input(
    "Amount",
    min_value=0.01,
    value=1.0
)

from_currency = st.sidebar.selectbox(
    "From",
    list(currencies.keys())
)

to_currency = st.sidebar.selectbox(
    "To",
    list(currencies.keys()),
    index=1
)

# Get exchange rate
url = f"https://api.frankfurter.dev/v2/rate/{from_currency.lower()}/{to_currency.lower()}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    rate = data["rate"]
    result = amount * rate

    st.header(
        f"{amount:g} {from_currency} = {result:.2f} {to_currency}"
    )

    st.write(f"1 {from_currency} = {rate:.4f} {to_currency}")

    st.divider()

    st.subheader("Conversion Table")

    table_amounts = [1, 5, 10, 50, 100, 500, 1000]

    table = []

    for value in table_amounts:
        converted = value * rate
        table.append({
            from_currency: value,
            to_currency: round(converted, 2)
        })

    st.table(table)

else:
    st.error("Could not get exchange rate.")