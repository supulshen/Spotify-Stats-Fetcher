# Spotify-Stats-Fetcher
A Python script to fetch your Spotify listening stats, including your top artists and tracks. Leverage the power of the Spotify Web API to gain insights into your music habits directly from your desktop.

## Features
- Retrieve your **Top Artists** and **Top Tracks** for different time ranges:
  - Short-term (4 weeks)
  - Medium-term (6 months)
  - Long-term (several years)
- User-friendly authentication using Spotify's OAuth 2.0.
- Customizable to include other Spotify data with minimal changes.

## Requirements
- Python 3.x
- A Spotify account
- Spotify Developer credentials (Client ID and Client Secret)

## Setup and Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/supulshen/spotify-stats-fetcher.git
   ```
2. Install dependencies:
   ```bash
   pip install spotipy
   ```
3. Configure your Spotify Developer credentials in the script:
   - Add your `Client ID`, `Client Secret`, and `Redirect URI`.

4. Run the script:
   ```bash
   python spotipy.py
   ```

5. Log in to your Spotify account in the browser when prompted, and view your stats in the console.

## Contributing
Feel free to open issues or submit pull requests to enhance this project. Contributions are welcome!

