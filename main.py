import streamlit as st
import pandas as pd
import os
import openai

# openai api intergration
openai.api_key = os.getenv('OPENAI_API_KEY')

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

st.write(gpt_response['choices'][0]['text'])
