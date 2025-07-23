# app.py

import streamlit as st
import cv2
import av
from roboflow import Roboflow
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# --- App Configuration ---
st.set_page_config(
    page_title="Live Coin Counter",
    page_icon="🪙",
    layout="centered"
)

# --- Roboflow Model Setup ---
# Use Streamlit's caching to load the model only once.
@st.cache_resource
def load_roboflow_model():
    """
    Loads and returns the Roboflow model using credentials from st.secrets.
    """
    try:
        # Access secrets from the .streamlit/secrets.toml file
        rf = Roboflow(api_key=st.secrets["ROBOFLOW_API_KEY"])
        project = rf.workspace().project(st.secrets["ROBOFLOW_PROJECT"])
        model = project.version(st.secrets["ROBOFLOW_VERSION"]).model
        return model
    except Exception as e:
        # Display an error if secrets are missing or incorrect
        st.error(f"Error loading Roboflow model: {e}. Please check your secrets.")
        return None

# --- Main Application UI ---
st.title("🪙 Live Coin Value Counter")
st.write("Point your camera at U.S. coins to see their total value calculated in real-time.")

# Load the model and define coin values
model = load_roboflow_model()
COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}

# --- Video Processing Class ---
class CoinCounterTransformer(VideoTransformerBase):
    """
    This class processes video frames to detect coins and calculate their value.
    """
    def __init__(self):
        self.model = model

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        """
        Receives a video frame, runs inference, draws results, and returns it.
        """
        # Return the frame immediately if the model isn't loaded
        if not self.model:
            return frame

        # Convert the video frame to a BGR NumPy array for OpenCV
        img = frame.to_ndarray(format="bgr24")

        # Run inference on the current frame
        results = self.model.predict(img, confidence=70, overlap=30).json()

        total_value = 0.0
        # Loop through each detected prediction
        for pred in results['predictions']:
            # Get bounding box coordinates
            x1 = int(pred['x'] - pred['width'] / 2)
            y1 = int(pred['y'] - pred['height'] / 2)
            x2 = int(pred['x'] + pred['width'] / 2)
            y2 = int(pred['y'] + pred['height'] / 2)
            class_name = pred['class']

            # Add to the total sum based on the detected class
            total_value += COIN_VALUES.get(class_name, 0.0)

            # Draw the bounding box on the image
            cv2.rectangle(img, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)
            # Draw the class label above the box
            cv2.putText(img, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display the total calculated value on the top-left of the frame
        total_text = f"Total Value: ${total_value:.2f}"
        cv2.putText(img, total_text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3, cv2.LINE_AA)

        # Convert the processed NumPy array back to a VideoFrame and return it
        return av.VideoFrame.from_ndarray(img, format="bgr24")

# --- Start the Stream ---
# Only start the streamer if the model was loaded successfully
if model:
    webrtc_streamer(
        key="coin-detector",
        video_transformer_factory=CoinCounterTransformer,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )
else:
    st.warning("Could not start video stream because the model failed to load.")