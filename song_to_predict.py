# Aritifical Intelligence CSC-4444
# Team 7 - Song Popularity Predictor
# Dataset generation source code: https://morioh.com/p/31b8a607b2b0

'''
from song_popularity_predictor import getTrackFeatures
import pandas as pd

track = getTrackFeatures('6rPO02ozF3bM7NnOV4h6s2')
dataset = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
dataset.to_csv("test.csv", sep = ',')
'''
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

# from song_popularity_predictor import getTrackFeatures
CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
# REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']
# Removed Redirect URI as it seemed it wasnt needed.
client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist= 'Moses Sumney'
track= 'Lonely World'

track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')
trackId = track_id['tracks']['items'][0]['id']
test = getTrackFeatures(trackId)
