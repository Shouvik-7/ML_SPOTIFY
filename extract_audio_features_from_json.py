import json
import pandas as pd
import numpy as np
import os

df = pd.read_csv('final.csv')
df['danceability'] = 0
df['acousticness'] = 0
df['energy'] = 0
df['instrumentalness'] = 0
df['liveness'] = 0
df['loudness'] = 0
df['speechiness'] = 0
df['tempo'] = 0
df['valence'] = 0
df.set_index('id',inplace=True)
df.drop('Unnamed: 0',axis=1,inplace=True)
for song in os.listdir('songs'):
    loc = 'songs/' + song
    f = open(loc)
    data = json.load(f)
    df.loc[loc.split("_")[1], ['danceability']] = data['danceability']
    df.loc[loc.split("_")[1], ['acousticness']] = data['acousticness']
    df.loc[loc.split("_")[1], ['energy']] = data['energy']
    df.loc[loc.split("_")[1], ['instrumentalness']] = data['instrumentalness']
    df.loc[loc.split("_")[1], ['liveness']] = data['liveness']
    df.loc[loc.split("_")[1], ['loudness']] = data['loudness']
    df.loc[loc.split("_")[1], ['speechiness']] = data['speechiness']
    df.loc[loc.split("_")[1], ['tempo']] = data['tempo']
    df.loc[loc.split("_")[1], ['valence']] = data['valence']

df.to_csv('final_dataset.csv')
