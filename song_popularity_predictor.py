# Aritifical Intelligence CSC-4444
# Team 7 - Song Popularity Predictor
# Dataset generation source code: https://morioh.com/p/31b8a607b2b0

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Gets track IDs from a specified user and playlist
def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

#Gets track features for a specified track ID
def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  popularity = meta['popularity']

  # features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']

  track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track

#Example playlist: 1,948 songs
#can add more to tailor dataset
ids = getTrackIDs('Ben', '6QAKnenuZoowNqxRzZbeRg?si=ca2f98299f464f57')

#Generates dataset based on ids defined above
def generate_dataset(sp_instance):
    # loop over track ids 
    tracks = []
    for i in range(len(ids)):
      time.sleep(.5)
      track = getTrackFeatures(ids[i])
      tracks.append(track)

    # create dataset
    dataset = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
    
    dataset.to_csv("dataset.csv", sep = ',')
    
    return dataset

if __name__ == '__main__':
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope='user-library-read'))
    print(sp.audio_analysis('6y0igZArWVi6Iz0rj35c1Y'))
    dset = generate_dataset(sp)
