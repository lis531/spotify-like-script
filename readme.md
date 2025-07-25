# Spotify Like Script
This script allows you to like the currently playing song on Spotify using the Spotipy library.

## Requirements
- Python 3.x
- Spotipy library
- Spotify account with an active session
- Spotify app registered in the Spotify Developer Dashboard

## Installation
### Automatic installation (recommended):
1. Download the repository.
2. Set up your Spotify app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
3. Set your redirect URI to `http://127.0.0.1:8888/callback`.
4. Run the `install.bat` file to install the required dependencies and set up the environment.
5. Follow the prompts to enter your Spotify credentials.

### Manual installation:
1. Download the repository.
2. Install Python 3.x from the [official website](https://www.python.org/downloads/).
3. Install the Spotipy library:
   ```bash
   pip install spotipy
   ```
4. Set up your Spotify app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
5. Set your redirect URI to `http://127.0.0.1:8888/callback`.
6. Obtain your `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` and place them in .env file:
   ```
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   ```

## Usage
To run the script, execute the launch.bat file.

## Note
If you use apps like Razer Synapse you may add the script to your macros to run it with a press of a key.
To do this:
1. Select a key.
<img width="652" height="631" alt="Selecting a key" src="https://github.com/user-attachments/assets/70c75db6-e2b9-4677-ae13-e43dede56978" />

2. Go into Launch category and select path to the launch.bat file.
<img width="1220" height="600" alt="Selecting launch.bat" src="https://github.com/user-attachments/assets/35925396-a8a4-489b-964e-bc9efb231ede" />

3. Save the macro.
