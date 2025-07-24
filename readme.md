# Spotify Like Script
This script allows you to like the currently playing song on Spotify using the Spotipy library.
## Requirements
- Python 3.x
- Spotipy library
- Spotify account with an active session
- Spotify app registered in the Spotify Developer Dashboard

## Installation
1. Install the Spotipy library:
   ```bash
   pip install spotipy
   ```
2. Set up your Spotify app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
3. Set your redirect URI to "http://127.0.0.1:8888/callback".
4. Obtain your `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` and place them in corresponding files:
   - `client_id.txt`
   - `client_secret.txt`
  
## Usage
To run the script, execute the launch.bat file.

## Note
If you use apps like Razer Synapse you may add the script to your macros to run it with a press of a key.
To do this:
1. Select a key
2. Go into Launch category
3. Select path to the launch.bat file.