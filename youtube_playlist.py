import os
from yt_dlp import YoutubeDL

def download_youtube_playlist_as_mp3(playlist_url, output_base_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(
            output_base_path,
            '%(playlist_title)s/%(title)s.%(ext)s'
        ),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True,
        'noplaylist': False,
        'yesplaylist': True,

        # 🔥 CRITICAL FIXES 🔥
        'extractor_args': {
            'youtube': {
                'player_client': ['android'],  # mobile client still works
                'player_skip': ['tv', 'web'],  # skip broken ones
            }
        },

        # Disable SABR streaming
        'youtube_include_dash_manifest': False,
        'youtube_include_hls_manifest': False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


youtube_playlist_url = "https://www.youtube.com/watch?v=qWWSM3wCiKY&list=PLTGr1FN7MjlvqRENEyxO2TABNpMVYgbDE"
output_base_directory = "./songs"

download_youtube_playlist_as_mp3(
    youtube_playlist_url,
    output_base_directory
)
