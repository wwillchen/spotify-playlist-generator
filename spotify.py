import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Authenticate the user
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='9fae11f38f7f4807bcf428baaf5ac0fc', client_secret='5954437d49ff46b8b38845077ce7a198', redirect_uri='http://localhost:8888/callback', scope='playlist-modify-public'))

# Create a new playlist

playlist_name = 'My 2 Another Playlist' # GET THIS FROM CHAT GPT
username = '31koa6e34uj5ztlwnzkl6obqxqom'
playlist = sp.user_playlist_create(username, playlist_name)

# Add tracks to the playlist
track_uris = ['spotify:track:6rPO02ozF3bM7NnOV4h6s2', 'spotify:track:7DFNE7NO0raLIUbgzY2rzm']
sp.playlist_add_items(playlist['id'], track_uris)

# Get link for playlist we just created
playlist_link = playlist['external_urls']['spotify']
print("Playlist link:", playlist_link)