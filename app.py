import os
import tempfile

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.title("🎤 AI Voice Language Tutor")

st.write("Speak a sentence and the AI will transcribe it.")

audio = st.audio_input(
    "🎙️ Record your sentence",
    sample_rate=16000
)

if audio:
    st.audio(audio)

    audio_bytes = audio.getvalue()

    st.info("🎧 Transcribing your sentence...")

    # Save recording as a temporary WAV file
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as temp_audio:

        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    try:
        # Upload audio to Gemini
        audio_file = client.files.upload(
            file=temp_audio_path
        )

        # Transcribe using Gemini 3.5 Transcribe
        interaction = client.interactions.create(
            model="gemini-3.5-transcribe",
            input=[
                {
                    "type": "audio",
                    "uri": audio_file.uri,
                    "mime_type": audio_file.mime_type,
                }
            ],
        )

        transcription = interaction.output_text

        st.subheader("📝 Your Sentence")
        st.write(transcription)

    except Exception as e:
        st.error(f"Transcription error: {e}")

    finally:
        os.remove(temp_audio_path)