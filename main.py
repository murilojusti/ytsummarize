from openai import OpenAI
import pytubefix
import os
from pytubefix import YouTube


def download_audio(url):
    try:
        yt = YouTube(url, on_complete_callback=True)
        stream = yt.streams.filter(only_audio=True).get_by_itag(251)
        print(yt.title)
        stream.download()

    except:
        print("Error downloading video")


def transcript_audio():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    transcription = client.audio.transcriptions.create(
        model= "gpt-4o-mini-transcribe", 
        file= open(audio_name, "rb")
    )

    print(transcription.text)

download_audio(input("Link: "))
transcript_audio()
