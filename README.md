# 🎥 YouTube Audio Summarizer with OpenAI

This project allows you to input a YouTube video URL, download the audio, convert it to `.mp3`, transcribe the content using OpenAI's Whisper API, and generate a concise summary using GPT. Ideal for quickly understanding long videos such as lectures, podcasts, and interviews.

---

## 📦 Features

- ✅ Download YouTube audio via URL
- ✅ Convert audio to `.mp3` using FFmpeg
- ✅ Transcribe audio with OpenAI Whisper (`gpt-4o-mini-transcribe`)
- ✅ Summarize transcribed content with GPT
- ✅ Works entirely from the command line
- ✅ Supports virtual environments and `.env` secrets

---

## 🧠 Technologies

- [`pytubefix`](https://pypi.org/project/pytubefix/) – for downloading YouTube audio
- [`ffmpeg-python`](https://github.com/kkroening/ffmpeg-python) – for audio processing
- [`static-ffmpeg`](https://pypi.org/project/static-ffmpeg/) – to ensure FFmpeg is available
- [`openai`](https://pypi.org/project/openai/) – for transcription and summarization

---

## ⚙️ Requirements

Before you run the project, make sure you:

- Have Python 3.9+ installed
- Have Git installed (for cloning)
- Use a virtual environment
- Provide your OpenAI API key in a `.env` file

---

## 📁 Folder Structure
```bash
ytsummarize/
├── main.py
├── requirements.txt
├── .gitignore
├── .env ← Not committed (contains your OpenAI API key)
```
---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/murilojusti/ytsummarize.git
cd ytsummarize
```
### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate     # On Linux/macOS
.venv\Scripts\activate        # On Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Create a .env file
Inside the project root, create a file called .env with the following content:
```bash
OPENAI_API_KEY=your_openai_key_here
```
🔒 Never commit this file. It is already ignored via .gitignore.

---

▶️ Running the Script
```bash
python main.py
```

You’ll be prompted to paste a YouTube URL. The script will:

Download the audio

Convert it to .mp3

Transcribe the speech to text

Summarize it using GPT

The summarized result will be printed in the terminal.

---

📝 Example Output
```bash
Link: https://www.youtube.com/watch?v=example123
Title: How Large Language Models Work

Transcription Summary:
This video explains the fundamentals of large language models...
```

## 📌 Prompt used for summarization

The summarization prompt is optimized for high-quality results. It instructs the AI to produce an objective, clear and complete summary of the video transcription in Portuguese or English, depending on the input language.

## 🛡️ Security & .env Handling

.env file is excluded from Git via .gitignore

Be sure to rotate your API key if it was exposed

Use git filter-repo to remove sensitive data from your history if needed

## 💡 Future Improvements

Create a simple web UI using Flask or Django

Add rate limiter

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## ✉️ Contact

Created by Murilo Justi Rodrigues – feel free to reach out!
