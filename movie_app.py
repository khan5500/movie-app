import streamlit as st
import numpy as np
import time

# Page Configuration
st.set_page_config(page_title="Cinematic Movie App", layout="centered")

# App Header
st.title("🎬 Cinematic Movie & Music App")
st.subheader("Welcome to your live Movie App!")

st.write("---")

# Video Player Section
st.markdown("### 📹 Video Player")
video_file = st.file_uploader("Upload your video file here", type=["mp4", "mov", "avi"])

if video_file is not None:
    st.video(video_file)
    st.success("Video loaded successfully!")

st.write("---")

# Audio Equalizer Section
st.markdown("### 🎵 Live Audio Equalizer Lights")
st.write("Click the button below to test the equalizer dots and lights effect:")

# Equalizer Animation Logic
if st.button("Turn ON Equalizer"):
    status_text = st.empty()
    chart_place = st.empty()
    
    for i in range(1, 20):
        # Generating random heights for red, green, and blue dots
        equalizer_data = np.random.randn(15, 3)
        chart_place.bar_chart(equalizer_data)
        status_text.text("⚡ Music Beats Active... Lights going up and down!")
        time.sleep(0.3)
        
    status_text.text("✅ Equalizer is ready and running!")
else:
    st.info("Press the button to see the equalizer lights dance.")
