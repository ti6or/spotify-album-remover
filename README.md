# Spotify Liked Albums Bulk Remover

A Python script to help you remove all your saved/liked albums (not individual songs) from your Spotify library after asking for confirmation. Useful if you want to clean up your library but find it tedious to do manually.

## ⚠️ WARNING ⚠️

* **This script PERMANENTLY removes albums from your Spotify library.**
* This action **CANNOT** be undone.
* It only affects **saved albums**, not saved/liked songs.
* Use this script **at your own risk**. The author is not responsible for any data loss.
* The script includes a confirmation step before deleting anything. Please read the prompts carefully.

## Features

* Fetches all your saved albums from Spotify.
* Prompts for explicit confirmation before deleting anything.
* Removes albums in batches to comply with Spotify API limits.
* Does **not** affect your saved/liked songs.

## Requirements

* Python 3 ([Installation Guide](https://www.python.org/downloads/))
* `pip` (Python package installer, usually included with Python 3)
* The `spotipy` library

## Setup Instructions

1.  **Install Python 3:** If you don't have it, download and install it from [python.org](https://www.python.org/downloads/). During installation, make sure to check the option "Add Python to PATH" if available.
2.  **Install Spotipy:** Open your Terminal (macOS/Linux) or Command Prompt/PowerShell (Windows) and run:
    ```bash
    pip3 install spotipy
    ```
    *(Use `pip` instead of `pip3` if `pip3` is not found but `pip` works for your Python 3 installation).*
3.  **Create a Spotify App:**
    * Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.
    * Click "Create App".
    * Give it a name (e.g., "My Album Remover") and a description. Check the terms checkbox.
    * Once created, you'll see your **Client ID**. Click "Show client secret" to see your **Client Secret**. You'll need both. **Keep your Client Secret safe like a password!**
    * Click "Edit Settings".
    * In the "Redirect URIs" section, add the following URI **exactly**:
        ```
        [http://127.0.0.1:9090](http://127.0.0.1:9090)
        ```
        *(Or `http://localhost:9090`. Make sure it matches the `REDIRECT_URI` you plan to use in the script).*
    * Scroll down and click **"Save"**.
4.  **Download the Script:**
    * On this GitHub repository page, click the green "<> Code" button, then choose "Download ZIP".
    * Extract the ZIP file. You'll find the `remove_albums.py` file inside.
    * Alternatively, if you know Git, you can clone the repository: `git clone https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories`
5.  **Configure the Script:**
    * Open the `remove_albums.py` file in a text editor (like VS Code, Sublime Text, Notepad++, TextEdit).
    * Find these lines near the top:
        ```python
        CLIENT_ID = 'XXX'
        CLIENT_SECRET = 'XXX'
        REDIRECT_URI = '[http://127.0.0.1:9090](http://127.0.0.1:9090)' # Or http://localhost:9090
        ```
    * Replace `'XXX'` for `CLIENT_ID` with **your own** actual Client ID (keep the quotes!).
    * Replace `'XXX'` for `CLIENT_SECRET` with **your own** actual Client Secret (keep the quotes!).
    * Ensure the `REDIRECT_URI` in the script matches **exactly** what you entered in the Spotify Dashboard settings.
    * Save the changes to the file.

## Usage

1.  **Open your Terminal or Command Prompt.**
2.  **Navigate to the directory** where you saved the `remove_albums.py` file using the `cd` command. For example:
    ```bash
    cd path/to/your/script/folder
    ```
3.  **Run the script:**
    ```bash
    python3 remove_albums.py
    ```
    *(Use `python` instead of `python3` if that's how you run Python 3 scripts on your system).*
4.  **First Run - Authentication:** Your web browser should open automatically, asking you to log in to Spotify and grant permission to the script (specifically, to view and modify your library). Accept the permissions. You'll be redirected to a `localhost` or `127.0.0.1` page which might show an error like "This site can’t be reached" - **this is usually normal**. The script has captured the necessary code from the URL. You can close that browser tab. The terminal should show "Successfully authenticated as...".
5.  **Album Fetching:** The script will start fetching your saved albums.
6.  **Confirmation:** Once all albums are found, it will display the total count and ask for **explicit confirmation** before deleting anything. Read the warning carefully!
7.  **Deletion:** If you type `yes` and press Enter, the script will proceed to remove the albums in batches. Otherwise, it will cancel the operation.

## Troubleshooting

* **`INVALID_CLIENT: Invalid redirect URI`:** This almost always means the `REDIRECT_URI` in your script does **not exactly match** the one you entered and saved in the Spotify Developer Dashboard settings for your app. Double-check both, ensure there are no typos or extra spaces, and make sure you clicked "Save" in the dashboard. Also, try deleting the `.cache` file in the same directory as the script and re-running it.
* **`command not found: python3` or `pip3`:** Make sure Python 3 is installed correctly and added to your system's PATH. Try using `python` or `pip` instead.
* **Other Errors:** Check your internet connection. Ensure your Client ID and Secret are correct.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
