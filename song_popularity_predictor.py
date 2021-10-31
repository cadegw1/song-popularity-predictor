# Aritifical Intelligence CSC-4444
# Team 7 - Song Popularity Predictor
import os
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']


if __name__ == '__main__':
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope='user-library-read'))
    print(sp.current_user())


