# Spotify Liked Albums Bulk Remover
# Author: ti6or
# Date: 2025-04-24
# Description: This script allows users to remove all their liked/saved albums
#              (not songs) from their Spotify library in bulk after confirmation.
#              Requires Python 3 and the spotipy library (pip3 install spotipy).

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import sys

# --- Configuration ---
# IMPORTANT: Replace 'XXX' with your own Client ID and Client Secret
# Get them from the Spotify Developer Dashboard: https://developer.spotify.com/dashboard/
# Add the Redirect URI exactly as below to your Spotify App settings.
CLIENT_ID = 'XXX'
CLIENT_SECRET = 'XXX'
REDIRECT_URI = 'http://127.0.0.1:9090' # Or 'http://localhost:9090' - must match dashboard

# --- Check Configuration ---
# Ensure placeholders are replaced before running
if 'XXX' in CLIENT_ID or 'XXX' in CLIENT_SECRET:
    print("ERROR: Please replace 'XXX' placeholders for CLIENT_ID and CLIENT_SECRET with your credentials.")
    sys.exit()

# --- Spotify API Scope ---
# Define the permissions needed: read and modify the user's library
SCOPE = 'user-library-read user-library-modify'

# --- Authentication ---
try:
    print("Attempting to authenticate...")
    # Authenticate using OAuth 2.0
    # This will open a browser window for login on the first run
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope=SCOPE,
                                                   open_browser=True))

    # Get current user's display name to confirm authentication
    user = sp.current_user()
    print(f"Successfully authenticated as: {user['display_name']} ({user['id']})")

except Exception as e:
    print(f"ERROR during authentication: {e}")
    print("Please check:")
    print("  1. Your internet connection.")
    print("  2. If CLIENT_ID and CLIENT_SECRET are correct.")
    print(f"  3. If REDIRECT_URI ('{REDIRECT_URI}') is added *exactly* to your app settings on the Spotify Developer Dashboard and saved.")
    sys.exit()

# --- Fetch Liked Albums ---
print("\nFetching your saved albums... This might take a while if you have many.")
all_albums = []
offset = 0
limit = 50 # Max albums per API request

while True:
    try:
        # Get a page of saved albums
        results = sp.current_user_saved_albums(limit=limit, offset=offset)
        albums_page = results['items']

        if not albums_page:
            break # No more albums found

        # Extract relevant info and add to the list
        for item in albums_page:
            album = item['album']
            # Handle cases where artist info might be missing (unlikely but safe)
            artist_name = album['artists'][0]['name'] if album['artists'] else "Unknown Artist"
            all_albums.append({
                'id': album['id'],
                'name': album['name'],
                'artist': artist_name
            })

        print(f"Found {len(all_albums)} albums so far...")
        offset += limit # Move to the next page

        # Check if it was the last page
        if len(albums_page) < limit:
            break

    except Exception as e:
        print(f"ERROR while fetching albums: {e}")
        sys.exit()

# --- Check if Albums Found ---
if not all_albums:
    print("\nNo saved albums found in your library.")
    sys.exit()

print(f"\nFound a total of {len(all_albums)} saved albums.")

# --- Confirmation Step ---
print("\n" + "="*50)
print("          !!! IMPORTANT WARNING !!!")
print("This script will PERMANENTLY remove saved albums.")
print("Liked/Saved SONGS will NOT be removed.")
print("This action CANNOT be undone.")
print("Review the total count above before proceeding.")
print("="*50)
confirm = input(f"Do you really want to remove all {len(all_albums)} saved albums from your library? Type 'yes' to confirm: ")

# --- Remove Albums (if confirmed) ---
if confirm.lower() == 'yes':
    print("\nRemoving albums...")
    album_ids_to_remove = [album['id'] for album in all_albums]

    removed_count = 0
    batch_size = 50 # Spotify API allows removing up to 50 albums per call

    # Process in batches
    for i in range(0, len(album_ids_to_remove), batch_size):
        batch_ids = album_ids_to_remove[i:i + batch_size]
        try:
            # Call the API to remove the current batch
            sp.current_user_saved_albums_delete(batch_ids)
            removed_count += len(batch_ids)
            print(f"Removed batch {i//batch_size + 1}. Total removed: {removed_count}")
        except Exception as e:
            print(f"ERROR removing batch {i//batch_size + 1}: {e}")
            print("Stopping the removal process.")
            break # Stop if an error occurs

    print(f"\nFinished. Successfully removed {removed_count} of {len(all_albums)} albums.")
else:
    print("\nOperation cancelled. No albums were removed.")