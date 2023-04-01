import streamlit as st
import pandas as pd
import config

# basic streamlit design
st.title('Testing design')
user_input = st.text_input('enter a user_input')
st.write('the user input is', user_input)