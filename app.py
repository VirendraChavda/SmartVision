import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import os
from PIL import Image
import numpy as np

# # Load YOLO Models
# object_detection_model = YOLO("yolo11s.pt")  # Replace with your object detection model path
# object_segmentation_model = YOLO("yolo11s-seg.pt")  # Replace with your segmentation model path
# pose_estimation_model = YOLO("yolo11s-pose.pt")  # Replace with your pose estimation model path

st.set_page_config(
    page_title="VisionFlow",  # Replace with your app name
    page_icon="assets/smart.png"  # Replace with a suitable emoji or a file path to an icon
)

# Preload models with caching
@st.cache_resource
def preload_models():
    return {
        "detection": YOLO("yolo11n.pt"),
        "segmentation": YOLO("yolo11n-seg.pt"),
        "pose": YOLO("yolo11n-pose.pt"),
    }

# Preloaded models
models = preload_models()

# Introduction Section
st.title("SmartVision App")
st.write("""
Welcome to the SmartVision app! This application allows you to:
1. Perform **Object Detection**.
2. Perform **Object Segmentation**.
3. Perform **Pose Estimation**.
         
Choose an input method (camera, video, or image) and see predictions live!
""")

# Model Selection
st.sidebar.title("Choose a Mode")
mode = st.sidebar.selectbox(
    "Select an application:",
    ("Object Detection", "Object Segmentation", "Pose Estimation")
)


# Input Method Selection
input_method = st.sidebar.radio(
    "Select Input Method:",
    ("Upload File", "Use Camera")
)

# Select the appropriate preloaded model based on the chosen mode
model = None
if mode == "Object Detection":
    model = models["detection"]
    st.sidebar.write("**Object Detection Mode Selected**")
elif mode == "Object Segmentation":
    model = models["segmentation"]
    st.sidebar.write("**Object Segmentation Mode Selected**")
elif mode == "Pose Estimation":
    model = models["pose"]
    st.sidebar.write("**Pose Estimation Mode Selected**")

# Function to process and predict image
def process_image(image, model):
    results = model(image)
    return results[0].plot()

def process_video(video_path, model):
    # Open the input video
    cap = cv2.VideoCapture(video_path)
    
    # Create a temporary file for the output video
    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4").name
    
    # Define codec and create VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for MP4 (H.264)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # Process the video frame by frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Run YOLO model prediction on the frame
        results = model(frame)
        annotated_frame = results[0].plot()  # Annotated frame
        
        # Write the annotated frame to the output video
        out.write(annotated_frame)
    
    # Release resources
    cap.release()
    out.release()
    
    return output_path  # Return the path to the processed video

# Handling File Upload
if input_method == "Upload File":
    uploaded_files = st.file_uploader(
        "Upload Images or Videos", 
        type=["jpg", "jpeg", "png", "mp4"], 
        accept_multiple_files=True  # Allow multiple file uploads
    )
    
    if uploaded_files:
        st.write("Files uploaded successfully.")
        
        # Show process button
        if st.button("Process Files"):
            for uploaded_file in uploaded_files:
                file_extension = uploaded_file.name.split(".")[-1]
                temp_file_path = tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}").name
                with open(temp_file_path, "wb") as f:
                    f.write(uploaded_file.read())
                
                if file_extension in ["jpg", "jpeg", "png"]:  # If it's an image
                    image = cv2.imread(temp_file_path)
                    annotated_image = process_image(image, model)
                    st.image(annotated_image, caption=f"Predicted Image: {uploaded_file.name}", use_container_width=True)
                elif file_extension == "mp4":  # If it's a video
                    st.write(f"Processing video: {uploaded_file.name}")
                    predicted_video_path = process_video(temp_file_path, model)  # Process video
                    st.success("Video processing completed!")
                    
                    # Provide download button
                    with open(predicted_video_path, "rb") as f:
                        st.download_button(
                            label="Download Processed Video",
                            data=f,
                            file_name=f"processed_{uploaded_file.name}",
                            mime="video/mp4"
                        )
                else:
                    st.warning(f"Unsupported file type: {uploaded_file.name}")

# Handling Camera Input
elif input_method == "Use Camera":
    st.write("Accessing your camera for live predictions. Press 'Stop' to exit.")
    
    # Start Camera Button
    run_camera = st.button("Start Camera", key="start_camera")
    if run_camera:
        cap = cv2.VideoCapture(0)  # Open camera
        stframe = st.empty()  # Create a placeholder for video feed
        stop_camera = False  # Initialize stop flag
        
        # Stop Camera Button
        stop_button = st.button("Stop Camera", key="stop_camera")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.warning("Failed to access the camera.")
                break
            
            # YOLO Predictions
            results = model(frame)
            annotated_frame = results[0].plot()
            
            # Display in Streamlit
            stframe.image(annotated_frame, channels="BGR", use_container_width=True)
            
            # Check if the "Stop Camera" button was clicked
            if stop_button:
                stop_camera = True
                break

        if stop_camera:
            cap.release()
            stframe.empty()  # Clear the video feed

# Footer Section
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: small;
        color: #6c757d;
    }
    </style>
    <div class="footer">
        Made using YOLOv11 models and Streamlit. © 2024 Virendrasinh Chavda. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)

