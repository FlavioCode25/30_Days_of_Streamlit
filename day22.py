import streamlit as st

st.title("st.form")

# Full example of using the with notation
st.header("1. Example of using 'with' notation")
st.subheader("Coffee machine")

with st.form("my_form"):
    st.subheader("**Order your coffee**")

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("Your order:")
        st.write(f"- Coffee bean: {coffee_bean_val}")
        st.write(f"- Coffee roast: {coffee_roast_val}")
        st.write(f"- Brewing method: {brewing_val}")
        st.write(f"- Serving format: {serving_type_val}")
        st.write(f"- Milk intensity: {milk_val}")
        st.write(f"- Bring own cup: {'Yes' if owncup_val else 'No'}")
    else:
        st.write('☝️ Place your order!')

# Short example of using an object notation

st.header("2. Example of using object notation")

form = st.form("my_form_2")
selected_val = form.slider("Select a value")
form.form_submit_button("Submit")

st.write(f"You selected: {selected_val}")