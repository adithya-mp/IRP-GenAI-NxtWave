# 🎤 AI Voice Language Tutor

An AI-powered language learning application that helps learners improve their grammar and vocabulary through voice interaction.

The user speaks a sentence in a selected language. The application converts the speech into text, uses Gemini AI to analyze the sentence, provides grammar and vocabulary feedback, generates a corrected sentence, and speaks the corrected sentence aloud.

---

## 🚀 Project Overview

The AI Voice Language Tutor follows this workflow:

🎤 User speaks  
↓  
📝 Speech-to-Text  
↓  
🤖 Gemini AI Grammar & Vocabulary Analysis  
↓  
✏️ Corrected Sentence  
↓  
🔊 Text-to-Speech  
↓  
🎧 User listens to the correction

---

## ✨ Features

- 🎙️ Record a sentence directly from the browser
- 📝 Convert speech into text
- 🌍 Select a target language
- 🤖 Detect grammar mistakes
- 📚 Analyze vocabulary and word choice
- ✏️ Generate a corrected sentence
- 💡 Provide a simple explanation of mistakes
- 🔊 Generate audio pronunciation of the corrected sentence
- 🌐 Supports multiple languages:
  - English
  - Hindi
  - Spanish
  - French
  - German

---

## 🛠️ Technologies Used

- Python 3.11
- Streamlit
- Google Gemini API
- Gemini Speech-to-Text
- Gemini LLM
- Gemini Text-to-Speech
- python-dotenv

---

## 🧠 AI Models Used

### Speech-to-Text
`gemini-3.5-transcribe`

Used to convert the learner's recorded voice into text.

### Language Analysis
`gemini-3.6-flash`

Used to analyze:

- Grammar
- Vocabulary
- Word choice
- Corrected sentence
- Simple explanations

### Text-to-Speech
`gemini-3.1-flash-tts-preview`

Used to generate audio for the corrected sentence.

---

## 📁 Project Structure

```text
AI-Voice-Language-Tutor/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── venv/