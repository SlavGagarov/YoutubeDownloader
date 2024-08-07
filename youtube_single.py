import os
from yt_dlp import YoutubeDL
from moviepy.editor import AudioFileClip

def download_youtube_video_as_mp3(url, output_path):
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
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"MP3 file saved in: {output_path}")

youtube_url = "https://www.youtube.com/watch?v=WPiEbYSF9kE"
output_directory = "./songs"
download_youtube_video_as_mp3(youtube_url, output_directory)