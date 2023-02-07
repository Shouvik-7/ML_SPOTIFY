from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
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


def search_for_track(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    if result.status_code == 200:
        json_result = result.json()
        return json_result
    else:
        print("Status error")
        return 1


playlist_ids = ['37i9dQZF1DX0yEZaMOXna3', '37i9dQZF1DX3Sp0P28SIer', '37i9dQZF1DX0h0QnLkMBl4', '37i9dQZF1DX9ukdrXQLJGZ',
                '37i9dQZF1DX8XZ6AUo9R4R', '37i9dQZF1DWTE7dVUebpUW', '37i9dQZF1DXe2bobNYDtW8', '37i9dQZF1DWVRSukIED0e9',
                '2fmTTbBkXi8pewbUvG3CeZ', '5GhQiRkGuqzpWZSE7OU4Se', '56r5qRUv3jSxADdmBkhcz7']

years = list(np.arange(2012, 2023))

token = get_token()
# print(token)

for id in enumerate(playlist_ids):
    print(id[0])
    print(id[1])
    j = search_for_track(token, id[1])

    with open(f"/playlists/top_hits_of_{years[id[0]]}_spotify.json", "w") as outfile:
        json.dump(j, outfile)
