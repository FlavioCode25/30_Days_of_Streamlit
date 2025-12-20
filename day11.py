import streamlit as st

st.header("st.multiselect")

options = st.multiselect(
    "What are your favorite colors?",
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write(f"You selected: {options}")

st.header("Day 12")
st.subheader("st.checkbox")

st.write("What would you like to order?")

icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("Great! Here is your ice cream 🍨")
if coffee:
    st.write("Okay, here's your coffee ☕")
if cola: 
    st.write("Sure! Enjoy your cola 🥤")

st.header("Day 15")
st.subheader("st.latex")
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

