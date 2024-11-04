import os
from yt_dlp import YoutubeDL

def download_youtube_playlist_as_mp3(playlist_url, output_base_path):
    ydl_opts_info = {
        'quiet': True,
        'extract_flat': True,
    }
    
    with YoutubeDL(ydl_opts_info) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
        playlist_title = info_dict.get('title', 'Playlist')

    output_path = os.path.join(output_base_path, playlist_title)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    print(f"MP3 files saved in: {output_path}")

youtube_playlist_url = "https://www.youtube.com/watch?v=NfaQl1IJoJs&list=PLTGr1FN7Mjlsv7Jj6ITGH5ImPkFCAWNJh"
output_base_directory = "./songs"
download_youtube_playlist_as_mp3(youtube_playlist_url, output_base_directory)
