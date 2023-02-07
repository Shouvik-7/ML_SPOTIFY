import json
import pandas as pd
import numpy as np
import os

df = pd.read_csv('final.csv')
genres_list = dict()
for artist in os.listdir('artistsdetails'):
    loc = 'artistsdetails/' + artist
    f = open(loc)
    data = json.load(f)

    genres_list[artist.split('.')[0]] = data['genres']
df['genres'] = df['artistid'].map(genres_list)

df.to_csv('final.csv')
