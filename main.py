from openai import OpenAI
import static_ffmpeg
import ffmpeg
import os
from pytubefix import YouTube

static_ffmpeg.add_paths()

def download_audio(url):
    try:
        yt = YouTube(url, on_complete_callback=True)
        stream = yt.streams.filter(only_audio=True).get_by_itag(251)
        print(yt.title)
        stream.download(filename="audio")
    except:
        print("Error downloading audio")

def convert_audio():

    (
        ffmpeg
        .input('audio')
        .filter('atempo', 2.5)
        .output('audio.mp3')
        .run()
    )

    print("Error converting audio")


def transcript_audio():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    transcription = client.audio.transcriptions.create(
        model= "gpt-4o-mini-transcribe", 
        file= open("audio.mp3", "rb")
    )

    print(transcription.text)

download_audio(input("Link: "))
convert_audio()
transcript_audio()