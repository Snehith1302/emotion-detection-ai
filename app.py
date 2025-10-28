# -------------------------------
# Imports
# -------------------------------
import os
import time
import tempfile
from PIL import Image
import numpy as np
import streamlit as st

# Optional packages
try:
    import cv2
except ImportError:
    cv2 = None
    st.warning("OpenCV not found. Webcam mode will be disabled.")

try:
    from deepface import DeepFace
except ImportError:
    DeepFace = None
    st.warning("DeepFace not found. Emotion detection will use fallback dummy results.")

# -------------------------------
# Streamlit page config
# -------------------------------
st.set_page_config(page_title="DeepFace Emotion Detection", layout="wide")
st.title("😊 DeepFace Emotion Detection")
st.write("Detect emotions in images or via webcam with confidence.")

# -------------------------------
# Emojis for each emotion
# -------------------------------
emotion_emojis = {
    "angry": "😠", "disgust": "🤢", "fear": "😨",
    "happy": "😄", "sad": "😢", "surprise": "😲", "neutral": "😐"
}

# -------------------------------
# Helper function for emotion analysis
# -------------------------------
def analyze_emotion(img_path):
    if DeepFace is None:
        return {
            'dominant_emotion': 'neutral',
            'emotion': {
                'angry': 0.0, 'disgust': 0.0, 'fear': 0.0,
                'happy': 0.0, 'sad': 0.0, 'surprise': 0.0, 'neutral': 100.0
            }
        }
    else:
        # Set enforce_detection=False to avoid face detection errors
        results = DeepFace.analyze(img_path=img_path, actions=['emotion'], enforce_detection=False)
        return results[0] if isinstance(results, list) else results

# -------------------------------
# Function to render emotion card with black text
# -------------------------------
def render_emotion_card(dominant_emotion, confidence):
    st.markdown(
       f"""
    <div style='
        background-color:#f0f0f5; 
        padding:15px; 
        border-radius:10px;
        color:black;
        font-size:20px;
        font-weight:bold;
    '>
        Detected Emotion: {dominant_emotion.capitalize()} {emotion_emojis.get(dominant_emotion,'')}<br>
        Confidence: {confidence:.2f}%
    </div>
    """, unsafe_allow_html=True
    )

# -------------------------------
# Tabs for Upload and Webcam
# -------------------------------
tab1, tab2 = st.tabs(["Upload Image", "Use Webcam"])

# -------------------------------
# Tab 1: Upload Image
# -------------------------------
with tab1:
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        image = Image.open(tmp_path).convert("RGB")

        col1, col2 = st.columns([2, 1])
        with col1:
            st.image(image, caption="Uploaded Image", use_container_width=True)
        with col2:
            with st.spinner("Analyzing emotions..."):
                try:
                    result = analyze_emotion(tmp_path)
                    dominant_emotion = result.get('dominant_emotion', 'unknown')
                    emotions = result.get('emotion', {}) or {}
                    confidence = emotions.get(dominant_emotion, 0.0)

                    # Render emotion card
                    render_emotion_card(dominant_emotion, confidence)

                    if emotions:
                        st.bar_chart(emotions)

                except Exception as e:
                    st.error(f"Error during analysis: {e}")

        os.remove(tmp_path)

# -------------------------------
# Tab 2: Webcam
# -------------------------------
with tab2:
    if cv2 is None:
        st.warning("Webcam mode disabled: OpenCV not installed.")
    else:
        st.write("Use your webcam to capture a single frame for emotion detection.")
        cam_image = st.camera_input("Capture image from webcam")

        if cam_image is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                tmp_file.write(cam_image.getvalue())
                tmp_path = tmp_file.name

            image = Image.open(tmp_path).convert("RGB")

            col1, col2 = st.columns([2, 1])
            with col1:
                st.image(image, caption="Captured Image", use_container_width=True)
            with col2:
                with st.spinner("Analyzing emotions..."):
                    try:
                        result = analyze_emotion(tmp_path)
                        dominant_emotion = result.get('dominant_emotion', 'unknown')
                        emotions = result.get('emotion', {}) or {}
                        confidence = emotions.get(dominant_emotion, 0.0)

                        # Render emotion card
                        render_emotion_card(dominant_emotion, confidence)

                        if emotions:
                            st.bar_chart(emotions)

                    except Exception as e:
                        st.error(f"Error during analysis: {e}")

            try:
                os.remove(tmp_path)
            except Exception:
                pass
