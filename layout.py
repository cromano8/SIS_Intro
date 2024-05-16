# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Get the current credentials
session = get_active_session()

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['','😄', '😆', '😊', '😍', '😴', '😕', '😱'])
tab1, tab2= st.tabs(['name','emoji'])

with tab1:
  if user_name != '':
    st.write(f'Hello {user_name}')
  else:
    st.write('Please enter your **name**!')

with tab2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favortie **emoji**!')
  else:
    st.write('Please choose an **emoji**!')
