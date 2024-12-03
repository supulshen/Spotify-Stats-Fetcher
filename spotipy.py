import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost:8888/callback"

# Define the scope for access
SCOPE = "user-top-read"

# Authenticate
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Fetch top artists
top_artists = sp.current_user_top_artists(limit=10, time_range="medium_term")
print("Top Artists:")
for idx, artist in enumerate(top_artists['items']):
    print(f"{idx + 1}: {artist['name']}")

# Fetch top tracks
top_tracks = sp.current_user_top_tracks(limit=10, time_range="medium_term")
print("\nTop Tracks:")
for idx, track in enumerate(top_tracks['items']):
    print(f"{idx + 1}: {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
