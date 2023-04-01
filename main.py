import streamlit as st
import pandas as pd
from config import API_Key
from dotenv import load_dotenv
import os
import openai

# openai api intergration
load_dotenv()
openai.api_key = os.getenv("$OPENAI_API_KEY")
st.write(os.getenv("OPENAI_API_KEY"))

# basic streamlit design
st.title('Testing design')
user_input = st.text_input('enter a user_input')

# takes user prompt into gpt
gpt_response = openai.Completion.create(
  model="text-davinci-003",
  prompt="provide a spotify song list for" + user_input,
  max_tokens=1000,
  temperature=1.5
)

# image generation
image = openai.Image.create(
  prompt=user_input,
  n=1,
  size="256x256"
)

image_url = image['data'][0]['url']
st.image(
    image_url,
    )
st.write(gpt_response['choices'][0]['text'])
