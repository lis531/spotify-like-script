import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-library-modify user-read-playback-state",
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://127.0.0.1:8888/callback"
))

track = spotify.current_playback()
if track and track.get("item"):
    spotify.current_user_saved_tracks_add([track["item"]["id"]])