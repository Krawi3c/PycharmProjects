from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime as dt
spotify_client_id = "bb15ff50f697467ab17b0e3812325afd"
spotify_client_secret = "22dad692f1564fd0a02127d8ff163e94"
response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")
content = response.text
soup = BeautifulSoup(content, "html.parser")
elements = soup.find_all(name="li", class_="o-chart-results-list__item")
song_names = []
for element in elements:
    title_item = element.find(name="h3", id="title-of-a-story")
    if title_item != None:
        title = title_item.getText().strip()
        song_names.append(title)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
date = dt.now().strftime("%Y-%m-%d")


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)