import streamlit as st
import requests
from requests.exceptions import RequestException

st.title('🏀 Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'https://www.boredapi.com/api/activity?type={selected_type}'
try:
  resp = requests.get(suggested_activity_url, timeout=5)
  resp.raise_for_status()
  suggested_activity = resp.json()
except RequestException as e:
  st.error(f"Request failed: {e}")
  suggested_activity = {"error": "Request failed"}

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)

if 'error' in suggested_activity:
  st.header('Suggested activity')
  st.error(suggested_activity.get('error'))
else:
  st.header('Suggested activity')
  st.info(suggested_activity.get('activity', 'No activity found.'))

  col1, col2, col3 = st.columns(3)
  with col1:
    participants = suggested_activity.get('participants')
    st.metric(label='Number of Participants', value=participants if participants is not None else 'N/A', delta='')
  with col2:
    t = suggested_activity.get('type')
    st.metric(label='Type of Activity', value=t.capitalize() if isinstance(t, str) else 'N/A', delta='')
  with col3:
    price = suggested_activity.get('price')
    st.metric(label='Price', value=price if price is not None else 'N/A', delta='')