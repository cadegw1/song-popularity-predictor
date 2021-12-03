Artificial Intelligence - CSC4444
Group 7 - Song Popularity Predictor

Summary:
    Repo contains two files: generate_dataset.py and song_popularity_predictor.py. The dataset generation script allows
    the user to pull songs and their feature sets from playlists. The song popularity predictor will use the generated 
    dataset to train and test its regression network. 

Required packages:
    - pandas
    - spotipy
    - pycaret
    - matplotlib

Included datasets:
    dataset.csv - Set containing 1949 samples from a playlist containing random songs
    SpotifyFeatures.csv - Set containing 228160 random samples from different genres

Feature set:
    - popularity (target)
    - genre (only included in the SpotifyFeatures dataset)
    - acousticness
    - danceability
    - duration_ms
    - energy
    - instrumentalness
    - key
    - liveness
    - loudness
    - mode
    - speechiness
    - temp
    - time_signature
    - valence