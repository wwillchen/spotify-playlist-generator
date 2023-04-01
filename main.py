import streamlit as st
import pandas as pd
from config import API_Key
import os
import openai

# openai api intergration
openai.api_key = API_Key


# basic streamlit design
st.title('Testing design')
user_input = st.text_input('enter a user_input')

# takes user prompt into gpt
gpt_response = openai.Completion.create(
  model="text-davinci-003",
  prompt=user_input,
  max_tokens=1000,
  temperature=1.5
)

st.write(gpt_response)
