# Musical-Time-Machine
This script scrapes the billboard hot 100 page (https://www.billboard.com/charts/hot-100/) for a specific date and creates a spotify playlist of the hot 100 songs for a particular date.

# Steps to use this script
1) Create a Spotify account or login to your Spotify account if you already have one.
2) Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App: https://developer.spotify.com/dashboard/
3) Once you've created a Spotify app, you would get a Client ID and Client Secret.
4) Create an env file by the name "env.env" and add the following entries to it:  
SPOTIPY_CLIENT_ID=your_client_id  
SPOTIPY_CLIENT_SECRET=your_client_secret  
SPOTIPY_REDIRECT_URI=http://example.com  
5) Run main.py and enter a date.  
6) Follow the steps shown on the screen and your Spotify playlist would be created.
