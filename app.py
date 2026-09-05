import os
import tempfile
import io
import wave
import base64

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def pcm_to_wav_bytes(pcm_data):
    buffer = io.BytesIO()

    with wave.open(buffer, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(pcm_data)

    return buffer.getvalue()

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

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as temp_audio:

        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    try:
        audio_file = client.files.upload(
            file=temp_audio_path
        )

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

        st.info("🤖 Analyzing your sentence...")

        feedback_response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"""
You are an English language tutor.

Analyze the learner's sentence:

"{transcription}"

Check:
1. Grammar mistakes
2. Vocabulary and word-choice mistakes
3. Give the corrected sentence
4. Give a short and simple explanation for a beginner.

Use exactly this format:

Corrected Sentence:
<corrected sentence>

Grammar:
<grammar feedback>

Vocabulary:
<vocabulary feedback>

Explanation:
<simple explanation>
"""
        )

        feedback = feedback_response.text

        corrected_sentence = feedback.split("Corrected Sentence:", 1)[1].split("Grammar:", 1)[0].strip()

        st.subheader("🤖 AI Tutor Feedback")
        st.write(feedback)

        st.subheader("🔊 Corrected Sentence")
        st.write(corrected_sentence)

        st.info("🔊 Generating pronunciation...")

        tts_interaction = client.interactions.create(
            model="gemini-3.1-flash-tts-preview",
            input=corrected_sentence,
            response_format={"type": "audio"},
            generation_config={
                "speech_config": [
                    {"voice": "Kore"}
                ]
            }
        )

        audio_data = base64.b64decode(
            tts_interaction.output_audio.data
        )

        wav_audio = pcm_to_wav_bytes(audio_data)

        st.audio(wav_audio, format="audio/wav")

    except Exception as e:
        st.error(f"Error: {e}")

    finally:
        os.remove(temp_audio_path)