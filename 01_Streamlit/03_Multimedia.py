# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st
from PIL import Image


# Images

# Load image from file
st.header("Image from file")
img = Image.open(".//assets//image.png") # change
st.image(img, caption="My Uploaded Image")
# Load image from URL
st.header("Image from URL")
img_url = "https://upload.wikimedia.org/wikipedia/commons/9/98/International_Pok%C3%A9mon_logo.svg"
st.image(img_url, caption="Image from URL")


# Audios

# Load audio from file
st.header("Audio from file")
audio_file = open(".//assets//audio.mp3", "rb") # change
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mpeg")
# Load audio from URL
st.header("Audio from URL")
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url)


# Videos 

# Load video from file
st.header("Video from file")
video_file = open(".//assets//video.mp4", "rb") # change
video_bytes = video_file.read()
st.video(video_bytes)
# Load video from URL
st.header("Video from URL")
video_url = "https://youtu.be/dQw4w9WgXcQ?si=twGniNRaP866vwoA"
st.video(video_url)
