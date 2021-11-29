import spotipy as sp
import os
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']


class SongPopularityPredictor:
    def __init__(self):
        client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
        self.client = sp.Spotify(client_credentials_manager=client_credentials_manager)

    def show_tracks(self, tracks, ids):
        for i, item in enumerate(tracks['items']):
            track = item['track']
            ids.append(track['id'])
        return ids

    def get_track_ids(self, user, playlist_id):
        ids = []
        playlist = self.client.user_playlist(user, playlist_id)
        tracks = playlist['tracks']
        self.show_tracks(tracks, ids)
        while tracks['next']:
            tracks = self.client.next(tracks)
            self.show_tracks(tracks, ids)
        return ids

    def get_track_features(self, id):
        meta = self.client.track(id)
        features = self.client.audio_features(id)

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

        track = [name, album, artist, release_date, length, popularity, danceability, acousticness,
                 energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
        return track

    def generate_dataset(self, size, ids, csv_name="dataset.csv"):
        print("Creating dataset ...")
        tracks = []
        for i in range(size):
            time.sleep(.2)
            track = self.get_track_features(ids[i])
            tracks.append(track)

        # create dataset
        dataset = pd.DataFrame(tracks, columns=['name', 'album', 'artist', 'release_date', 'length', 'popularity',
                                                'danceability', 'acousticness', 'danceability', 'energy',
                                                'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo',
                                                'time_signature'])

        # using pandas, write out dataset to .csv file
        dataset.to_csv(csv_name, sep=',')

    def get_song_features(self, artist, track):
        track = self.client.search(q='artist:' + artist + ' track:' + track, type='track')
        track_id = track['tracks']['items'][0]['id']
        return self.get_track_features(track_id)

