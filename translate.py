!pip install googletrans

import streamlit as st
from googletrans import Translator

translator = Translator()

st.title("Google Translate in Streamlit")

text = st.text_input("Enter text to translate:")

if text:
    language = st.selectbox("Select language to translate to:",
                            ["Arabic", "German", "Spanish", "French", "Italian", "Japanese", "Korean", "Russian"])

    if language == "Arabic":
        dest = "ar"
    elif language == "German":
        dest = "de"
    elif language == "Spanish":
        dest = "es"
    elif language == "French":
        dest = "fr"
    elif language == "Italian":
        dest = "it"
    elif language == "Japanese":
        dest = "ja"
    elif language == "Korean":
        dest = "ko"
    elif language == "Russian":
        dest = "ru"
    else:
        dest = "en"

    translated_text = translator.translate(text, dest=dest).text

    st.write("Translated Text:")
    st.write(translated_text)
