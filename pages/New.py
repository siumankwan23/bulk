import streamlit as st
from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=lang)

        # Save the audio to a temporary file
        output_file = "output.mp3"
        tts.save(output_file)

        return output_file
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

st.title("Text to Speech Converter")

# Input text area
text = st.text_area("Enter text to convert:", "")

# Language selection
language = st.selectbox("Select language:", ["en", "fr", "es"])  # Add more languages as needed

if st.button("Convert to Speech"):
    if text.strip() != "":
        output_file = text_to_speech(text, lang=language)
        if output_file:
            st.audio(output_file, format="audio/mp3")
            st.download_button(
                label="Download Audio",
                data=open(output_file, "rb").read(),
                file_name="output.mp3",
                mime="audio/mp3"
            )
            os.remove(output_file)  # Remove temporary file after playing
    else:
        st.warning("Please enter some text to convert.")
