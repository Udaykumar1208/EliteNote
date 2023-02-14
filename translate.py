import streamlit as st
import whisper
import tempfile


st.title("Audio Transcription and Translation with Whisper")

model = whisper.load_model("base")

audio_file = st.file_uploader("Choose a file", type= ["wav","mp3","m4a"])
if audio_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(audio_file.getbuffer())
        st.success("Saved File")

        if st.sidebar.button("Transcribe"):
            if audio_file is not None:
                st.sidebar.text("Transcribing...")
                st.sidebar.text(temp.name)
                transcript = model.transcribe(temp.name)
                st.sidebar.success("Transcription complete")
                st.write(transcript["text"])
            else:
                st.error("Please Upload an Audio File")
