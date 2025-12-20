import streamlit as st

st.header("st.selectbox")

option = st.selectbox(
    "What is your favorite color?",
    ("Blue", "Red", "Green")
)

st.write(f"Your favorite color is {option}")