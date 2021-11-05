# Aritifical Intelligence CSC-4444
# Team 7 - Song Popularity Predictor
import os
import numpy as np
import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']


if __name__ == '__main__':
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope='user-library-read'))
    print(sp.audio_analysis('6y0igZArWVi6Iz0rj35c1Y'))




    """
    Alternate method using requests
    """
    # AUTH_URL = 'https://accounts.spotify.com/api/token'
    #
    # # POST
    # auth_response = requests.post(AUTH_URL, {
    #     'grant_type': 'client_credentials',
    #     'client_id': CLIENT_ID,
    #     'client_secret': CLIENT_SECRET,
    # })
    #
    # # convert the response to JSON
    # auth_response_data = auth_response.json()
    #
    # # save the access token
    # access_token = auth_response_data['access_token']
    #
    # headers = {
    #     'Authorization': 'Bearer {token}'.format(token=access_token)
    # }
    #
    # # base URL of all Spotify API endpoints
    # BASE_URL = 'https://api.spotify.com/v1/'
    #
    # # Track ID from the URI
    # track_id = '6y0igZArWVi6Iz0rj35c1Y'
    #
    # # actual GET request with proper header
    # r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    # print(r.json())
