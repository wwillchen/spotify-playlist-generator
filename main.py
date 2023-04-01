import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
import openai

# openai api intergration
load_dotenv()
openai.api_key = os.getenv('API_Key')

# basic streamlit design
import streamlit as st

st.title('AI Spotify playlist generator')

with st.sidebar:
    Mood = st.slider(
        'Around what would you rate your mood from 0 (Sad/Somber) to 1 (Happy/Cheerful)?',
        0.0, 1.0, (0.2, 0.5))

    Tempo = st.slider(
        'What Tempo music are you looking for?',
        0.0, 150.0, (25.0, 75.0))
    
    status = st.radio('Select the type of music you want: ',
		('Instrumental', 'Vocal'))
    options = st.radio('options', ('High Energy', 'Relaxed/Mellow'), label_visibility='collapsed')
    

    if st.button('Save Configuration'):
        st.write('We will try to find music that matches your preferences:')
        st.write('Mood: ', Mood)
        st.write('Tempo: ', Tempo)
        st.write('Type: ', options, status, " music")
        Mud = Mood
        Tump = Tempo
        Stump = status
        Optump = options

    else:
        st.write('Please save a configuration')
        

user_input = st.text_input('What would you like to listen to?')

# takes user prompt into gpt
gpt_response = openai.Completion.create(
  model="text-davinci-003",
  prompt="provide a list of spotify track URI related to" + user_input,
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

song_URIs = gpt_response['choices'][0]['text'].splitlines()

