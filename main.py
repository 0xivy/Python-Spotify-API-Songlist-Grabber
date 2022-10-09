import requests
import base64
from secrets import clientID, clientSecret
import json


authurl = "https://accounts.spotify.com/api/token"
authheaders ={}
authdata ={}


def getAccessToken(clientID, clientSecret):
    message = f"{clientID}:{clientSecret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    authheaders['Authorization'] = "Basic " + base64_message
    authdata['grant_type'] = "client_credentials"
    res = requests.post(authurl, headers=authheaders, data=authdata)
    responseObject = res.json()
    accessToken = responseObject['access_token']
    return accessToken


def getPlaylistTracks(accessToken, playlistID):
    playlistEndpoint = f"https://api.spotify.com/v1/playlists/{playlistID}"
    getHeader = {
        "Authorization": "Bearer " + token
    }
    res = requests.get(playlistEndpoint, headers=getHeader)
    playlistObject = res.json()
    return playlistObject

#Api requests
token = getAccessToken(clientID, clientSecret)
playlistID = "28QFEnG9HFDquttvtIORn1?si=373f66028f7a48b0"

tracklist = getPlaylistTracks(token,playlistID)
trackListv2 = tracklist['tracks']['items']

songList =[]
for x in trackListv2:
    song = x['track']['name']
    songList.append(song)
with open(r'SongList.txt', 'w') as fp:
    for item in songList:
        fp.write("%s\n" % item)
    print('Done')
