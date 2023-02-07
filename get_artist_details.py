from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import time
import pandas as pd
import numpy as np

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def artistdetails_for_track(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    if result.status_code == 200:
        json_result = result.json()
        return json_result
    else:
        print("Status error")
        return 1

token = get_token()
#print(token)

df = pd.read_csv('final.csv')


for artist in df['artistid']:
    data = artistdetails_for_track(token, artist)
    if data != 1:
        #data = artistdetails_for_track(token, artist)
        with open(f"artistsdetails/{artist}.json", "w") as outfile:
            json.dump(data, outfile)
    else:
        print("waiting")
        time.sleep(240)
        print("Wait over")
        data = artistdetails_for_track(token, artist)
        if data != 1:
            data = artistdetails_for_track(token, artist)
            with open(f"artistsdetails/{artist}.json", "w") as outfile:
                json.dump(data, outfile)