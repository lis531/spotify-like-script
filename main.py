import os, sys, requests
from io import BytesIO
from PIL import Image, ImageDraw
from dotenv import load_dotenv
from winotify import Notification
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()

NOTIFY = os.getenv("NOTIFICATIONS_ENABLED", "true").lower() == "true"

spotify = Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-library-modify user-library-read user-read-playback-state"
))

track = spotify.current_playback()
track_id = track["item"]["id"]
track_name = track["item"]["name"]
liked = spotify.current_user_saved_tracks_contains([track_id])[0]

def get_album_cover():
    if not track:
        return None
    item = track.get("item")
    if not item:
        return None
    url = item["album"]["images"][0]["url"]
    img = Image.open(BytesIO(requests.get(url).content)).resize((128, 128), Image.LANCZOS)
    mask = Image.new('L', img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *img.size), radius=16, fill=255)
    icon_img = Image.new('RGBA', img.size)
    icon_img.paste(img, (0, 0))
    icon_img.putalpha(mask)
    icon_path = os.path.abspath("album_icon.ico")
    icon_img.save(icon_path, format="ICO", sizes=[(64, 64)])
    return icon_path

if "-dislike" in sys.argv:
    if liked:
        spotify.current_user_saved_tracks_delete([track_id])
        header = "Removed from liked"
    else:
        header = "Track was not liked"
else:
    if liked:
        header = "Track already liked"
    else:
        spotify.current_user_saved_tracks_add([track_id])
        header = "Liked"

if NOTIFY:
    icon = get_album_cover()
    Notification(
        app_id="Spotify Liked Toggle",
        title=header,
        msg=track_name,
        icon=icon
    ).show()