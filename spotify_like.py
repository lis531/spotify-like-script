import spotipy
from spotipy.oauth2 import SpotifyOAuth
from plyer import notification
import os
from dotenv import load_dotenv
load_dotenv()

def show_notification(message):
    notification.notify(
        title="Spotify like script",
        message=message,
        app_name="Spotify Like Script",
        timeout=5,
        app_icon="spotify.ico"
    )

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-library-modify user-library-read user-read-playback-state",
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://127.0.0.1:8888/callback"
))

NOTIFICATIONS_ENABLED = os.getenv("NOTIFICATIONS_ENABLED", "true").lower() == "true"

track = spotify.current_playback()
if track and track.get("item"):
    if NOTIFICATIONS_ENABLED:
        show_notification(f"Track already liked: {track['item']['name']}")
    if not spotify.current_user_saved_tracks_contains([track["item"]["id"]])[0]:
        spotify.current_user_saved_tracks_add([track["item"]["id"]])
        if NOTIFICATIONS_ENABLED:
            show_notification(f"Liked: {track['item']['name']}")
else:
    if NOTIFICATIONS_ENABLED:
        show_notification("No track is currently playing")