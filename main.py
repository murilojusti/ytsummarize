import openai
import pytubefix
from pytubefix import YouTube
import ffmpeg

def download_audio(url):
    try:
        yt = YouTube(url, on_complete_callback=True)
        stream = yt.streams.filter(only_audio=True).get_by_itag(251)
        stream.download()
    except:
        print("Error downloading video")