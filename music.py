load_dotenv()

API_ID = int(os.getenv("API_ID"))

API_HASH = os.getenv("API_HASH")

SESSION_NAME = os.getenv("SESSION_NAME")

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)@app.on_message(filters.audio & ~filters.edited & filters.chat(int(CHAT_ID)))

async def play_music(client, message):

    # Get the audio message

    audio_file = await message.download()

    # Join the voice chat

    group_call = await app.create_group_call(int(CHAT_ID))

    # Start playing the audio file in the voice chat

    audio = AudioSegment.from_file(audio_file)

    audio.export("audio.raw", format="raw")

    await group_call.start_audio_call("audio.raw", enable_p2p=True)

    # Wait for the audio to finish playing

    duration = len(audio) / 1000

    await asyncio.sleep(duration)

    # Leave the voice chat

    await group_call.stop_audio_call()

    await group_call.leave_group_call()

if __name__ == '__main__':

    app.run()


