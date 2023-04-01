import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import openai

# openai api intergration
load_dotenv()
openai.api_key = os.getenv('API_Key')

def create_playlist(pl_name):
    # Create a new playlist
    playlist_name = pl_name # GET THIS FROM CHAT GPT
    username = '31koa6e34uj5ztlwnzkl6obqxqom'
    playlist = sp.user_playlist_create(username, playlist_name)

    # Add tracks to the playlist
    track_uris = song_URIs
    sp.playlist_add_items(playlist['id'], track_uris)

    # Get link for playlist we just created
    playlist_link = playlist['external_urls']['spotify']
    print("Playlist link:", playlist_link)

# web layout
st.title(':green[Spotify playlist generator]')
# allows user to narrow song search
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
  prompt="provide a list of spotify track URI related to" + user_input + "then provide me a name for the playlist",
  max_tokens=1000,
  temperature=1
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

playlist = gpt_response['choices'][0]['text'].splitlines()
song_URIs = playlist[:-1]
playlist_title = playlist[-1]

# Authenticate the user
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='9fae11f38f7f4807bcf428baaf5ac0fc', client_secret='5954437d49ff46b8b38845077ce7a198', redirect_uri='http://localhost:8888/callback', scope='playlist-modify-public'))

create_playlist(playlist_title)