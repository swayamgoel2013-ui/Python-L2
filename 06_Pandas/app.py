import streamlit as st
import pandas as pd

df = pd.read_csv("dataset.csv")

st.header("Using `st.table`")
st.table(df)        # static table
st.header("Using `st.dataframe`")
st.dataframe(df)    # interactive table
st.header("Using `st.write`")
st.write(df)        # interactive table