import spotipy as sp
import os
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']


# Authorize with spotify api
def authorize():
    client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    client = sp.Spotify(client_credentials_manager=client_credentials_manager)
    return client


# Return list of features for a given track
def get_track_features(client, id):
    meta = client.track(id)
    features = client.audio_features(id)

    # meta
    track_name = meta['name']
    track_id = meta['id']
    artist_name = meta['album']['artists'][0]['name']
    duration_ms = meta['duration_ms']
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
    valence = features[0]['valence']
    mode = features[0]['mode']
    key = features[0]['key']

    track = [artist_name, track_name, track_id, popularity, acousticness, danceability, duration_ms, energy,
             instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time_signature, valence]
    return track


# Extends ids array
def show_tracks(tracks, ids):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        ids.append(track['id'])
    return ids


# Gets track IDs from a specified user and playlist
def get_track_ids(client, user, playlist_id):
    ids = []
    playlist = client.user_playlist(user, playlist_id)
    tracks = playlist['tracks']
    show_tracks(tracks, ids)
    while tracks['next']:
        tracks = client.next(tracks)
        show_tracks(tracks, ids)
    return ids


# Generate dataset and put it into a csv
def generate_dataset(client, size, ids, csv_name="dataset.csv"):
    print("Creating dataset ...")
    tracks = []
    for i in range(size):
        track = get_track_features(client, ids[i])
        tracks.append(track)

    # create dataset
    dataset = pd.DataFrame(tracks, columns=['artist_name', 'track_name', 'track_id', 'popularity',
                                            'acousticness', 'danceability', 'duration_ms', 'energy',
                                            'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
                                            'speechiness', 'tempo', 'time_signature', 'valence'])

    # using pandas, write out dataset to .csv file
    dataset.to_csv(csv_name, sep=',')


if __name__ == '__main__':
    client = authorize()
    ids = get_track_ids(client, 'Ben', '6QAKnenuZoowNqxRzZbeRg?si=ca2f98299f464f57')
    dataset_size = 100
    csv_name = 'dataset.csv'
    generate_dataset(client, dataset_size, ids, csv_name)
