from openai import OpenAI
import static_ffmpeg
import ffmpeg
import os
from pytubefix import YouTube

static_ffmpeg.add_paths()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def download_audio(url):
    try:
        yt = YouTube(url, on_complete_callback=True)
        stream = yt.streams.filter(only_audio=True).get_by_itag(251)
        print(yt.title)
        stream.download(filename="audio")
    except:
        print("Error downloading audio")

def convert_audio():
    download_audio(input("Link: "))
    (
        ffmpeg
        .input('audio')
        .filter('atempo', 2.5)
        .output('audio.mp3')
        .run()
    )

    print("Error converting audio")


def transcript_audio():
    convert_audio()
    transcription = client.audio.transcriptions.create(
        model= "gpt-4o-mini-transcribe", 
        file= open("audio.mp3", "rb")
    )
    return transcription.text

def summarize_video():
    transcrition = transcript_audio()
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "developer",
            "content": 'Summarize the transcript of a YouTube video clearly and objectively, highlighting the main points, avoiding repetition, calls to action, or names of hosts, in order to make the reading and comprehension as easier as possible. If possible, organize with bullet points. ALWAYS summarize in the same language as the transcription given'
        },
        {
            "role": "user",
            "content": transcrition
        }
    ]
)
    print(completion.choices[0].message.content)


summarize_video()