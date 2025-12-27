import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError

st.title('st.secrets')

try:
	secret = st.secrets['This is a streamlit secret message!']
except StreamlitSecretNotFoundError:
	secret = 'No secrets file found — create .streamlit/secrets.toml'
except KeyError:
	secret = 'Secret key not found in .streamlit/secrets.toml'

st.write(secret)