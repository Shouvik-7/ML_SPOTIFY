import json
import pandas as pd
import numpy as np


def get_year_dataFrame(json_data, year):
    dict_song = {"name": [],
                 "artists": [],
                 "artistid":[],
                 "id": [],
                 "explicit": [],
                 "popularity": [],
                 "durationms": []}
    for track in json_data['tracks']['items']:
        artist_names = []
        dict_song['id'].append(track['track']['id'])
        dict_song['name'].append(track['track']['name'])
        dict_song['explicit'].append(track['track']['explicit'])
        for artist in track['track']['artists']:
            artist_names.append(artist['name'])
        dict_song['artists'].append(artist_names)
        dict_song['artistid'].append(track['track']['artists'][0]['id'])
        dict_song['popularity'].append(track['track']['popularity'])
        dict_song['durationms'].append(track['track']['duration_ms'])
    df = pd.DataFrame(dict_song)
    df['year'] = year
    print(df)
    return df


file_names = ['top_hits_of_2012_spotify.json', 'top_hits_of_2013_spotify.json', 'top_hits_of_2014_spotify.json',
              'top_hits_of_2015_spotify.json', 'top_hits_of_2016_spotify.json', 'top_hits_of_2017_spotify.json',
              'top_hits_of_2018_spotify.json', 'top_hits_of_2019_spotify.json', 'top_hits_of_2020_spotify.json',
              'top_hits_of_2021_spotify.json', 'top_hits_of_2022_spotify.json']
years = list(np.arange(2012, 2023))

df_final = pd.DataFrame()
for i in enumerate(file_names):
    # Opening JSON file
    f = open('playlists/'+i[1])
    data = json.load(f)
    df = get_year_dataFrame(data, years[i[0]])
    df_final = pd.concat([df_final, df])
df_final.to_csv('final.csv')
