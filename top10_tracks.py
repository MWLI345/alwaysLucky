import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
import spotipy.util as util
import pandas as pd
from tabulate import tabulate
#from pandasgui import show

#Need to input your own client id and client secret
cid = ""
secret = ""
redirect_uri = ''

os.environ['SPOTIPY_CLIENT_ID']= cid
os.environ['SPOTIPY_CLIENT_SECRET']= secret
os.environ['SPOTIPY_REDIRECT_URI']= redirect_uri


#Authenticate Spotify Credentials and pull data
username = ""
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(limit=10,offset=0,time_range='medium_term')

#Process and clean the pulled information
songs_list = results['items']

top_10_artists = []
top_10_songs = []
for index, element in enumerate(songs_list):
    top_10_artists.append(element['artists'][0]['name'])
    top_10_songs.append(songs_list[index]['name'])

data = {'Song': top_10_songs, 'Artist': top_10_artists}
df = pd.DataFrame(data)

print(tabulate(df, headers='keys', tablefmt='psql'))
#show(df)