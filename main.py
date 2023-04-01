import streamlit as st
import pandas as pd
from config import API_Key
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# basic streamlit design
st.title('Testing design')
user_input = st.text_input('enter a user_input')
st.write('the user input is', user_input)

# openai api intergration

# takes user prompt into gpt
