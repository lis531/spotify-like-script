import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = open("client_id.txt").read().strip()
SPOTIPY_CLIENT_SECRET = open("client_secret.txt").read().strip()

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-library-modify user-read-playback-state",
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri="http://127.0.0.1:8888/callback"
))

track = spotify.current_playback()
if track and track['item']:
    spotify.current_user_saved_tracks_add([track['item']['id']])
    print(f"❤️  Liked: {track['item']['name']}")
else:
    print("⚠️ No song playing")