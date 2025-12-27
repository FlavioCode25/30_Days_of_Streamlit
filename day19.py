import streamlit as st

st.set_page_config(layout="wide")

st.title("How to layout your Streamlit app")

with st.expander("About this app"):
    st.write("This app shows the various ways on how you can layout your Streamlit app.")
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header("input")
user_name = st.sidebar.text_input("What is your name?")
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header("Output")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Name")
    if user_name != "":
        st.write(f" 👋 Hello, {user_name}!")
    else:
        st.write('👈  Please enter your **name**!')
with col2:
    st.subheader("Emoji")
    if user_emoji != "":
        st.write(f"{user_emoji} You have selected this **emoji**.")
    else:
        st.write('👈  Please select an **emoji**!')
with col3:
    st.subheader("Food")
    if user_food != "":
        st.write(f"🍽️ Your favorite **food** is {user_food}.")
    else:
        st.write('👈  Please select your favorite **food**!')