from pyrogram import Client, filters

from pyrogram.types import Message

import os

import youtube_dl

import ffmpeg

app = Client(session_name=os.environ.get("SESSION_NAME"), api_id=os.environ.get("API_ID"), api_hash=os.environ.get("API_HASH"))def download_audio(video_url):

    ydl_opts = {

        "format": "bestaudio/best",

        "quiet": True,

        "outtmpl": "audio.%(ext)s",

        "postprocessors": [{

            "key": "FFmpegExtractAudio",

            "preferredcodec": "mp3",

            "preferredquality": "192",

        }],

    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        ydl.download([video_url])

    return "audio.mp3"def play_audio(client, message, audio_file):

    chat_id = message.chat.id

    voice_chat = message.voice_chat

    if not voice_chat:

        message.reply_text("Please join a voice chat first!")

        return

    try:

        with open(audio_file, "rb") as f:

            client.send_voice(chat_id, voice_chat.id, f, duration=30)

    except Exception as e:

        message.reply_text(f"An error occurred while playing the audio: {e}")

    os.remove(audio_file)
    @app.on_message(filters.command("play") & filters.private)

def play(client, message):
