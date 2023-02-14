import spotipy
import spotipy.util as util

scope = 'user-library-read'


# Get username from terminal
username = input("Enter your Spotify username: ")


# Get client ID and secret from Spotify API
CLIENT_ID = "a15374d0d68a419180ee8093fe2cd900"
CLIENT_SECRET = "11b822ab03634c9cae69b3dafa585ae5"




# Get a token
token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri='http://localhost:8888/callback')
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)





