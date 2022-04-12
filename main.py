import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="env.env")
SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope))

print(sp.current_user()["id"])

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
res = requests.get(url)
res.raise_for_status()
content = res.text

soup = BeautifulSoup(content, "html.parser")
chart_items = soup.find_all(name="ul",
                            class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")

titles = []
labels = []
for chart_item in chart_items:
    title = chart_item.find(name="h3", id="title-of-a-story").string[1:-1]
    label = chart_item.find(name="span", class_="c-label").string[1:-1]
    titles.append(title)
    labels.append(label)
uri_list = []
print(titles)
print(labels)
for i in range(len(titles)):
    search_res = sp.search(q=f"{titles[i]} {labels[i]}", limit=1, type="track")
    try:
        uri_list.append(search_res["tracks"]["items"][0]["uri"])
    except IndexError:
        pass

print(uri_list)
playlist = sp.user_playlist_create(user=sp.current_user()["id"], name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)
