# SmartVision App [Click Here](https://smart-vision-1058693665617.europe-west1.run.app/)
### Author: Virendrasinh Chavda

<p align="justify">
This repository contains a cutting-edge computer vision application built with Streamlit and YOLOv11 models. The app allows users to perform object detection, segmentation, and pose estimation on images or videos. With an interactive interface, users can upload files or use live camera input to see real-time predictions.
</p>

![Results](yolo1.gif)
---

## Table of Contents
1. [Overview](#Overview)
2. [Installation](#Installation)
3. [Features](#Features)
4. [Usage](#Usage)
5. [Methodology](#Methodology)
6. [Future Work](#Future-Work)
7. [Contributing](#Contributing)
8. [License](#License)

---

## Overview
<p align="justify">
SmartVision App is a versatile vision-based tool designed for object detection, object segmentation, and pose estimation. By leveraging YOLOv11 models, the app provides real-time predictions with high accuracy. It supports images, videos, and live camera input, making it ideal for researchers, developers, and enthusiasts interested in computer vision.
</p>

---

## Installation

To set up and use this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/smartvision-app.git
   cd smartvision-app
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Features

### Object Detection
- Detect objects in uploaded images or videos.
- Real-time predictions on live camera feed.

### Object Segmentation
- Segment objects and visualize boundaries on uploaded files or live feed.

### Pose Estimation
- Predict human poses with keypoints and skeletons.

### Interactive Input
- Upload multiple images/videos (JPG, PNG, MP4).
- Use a live camera for instant predictions.

### Download Processed Outputs
- Save annotated images or videos with a single click.

---

## Usage

1. <strong>Launch the App</strong>:
   - Run `streamlit run app.py` in your terminal.
   - The app will open in your default web browser.

2. <strong>Choose a Mode</strong>:
   - Use the sidebar to select one of the three modes:
     - Object Detection
     - Object Segmentation
     - Pose Estimation

3. <strong>Select Input Method</strong>:
   - Upload files or use the live camera.

4. <strong>Get Predictions</strong>:
   - Process files to see annotated results.
   - Download annotated videos or images.

---

## Methodology

### YOLOv11 Models
- <strong>Object Detection</strong>: Model file: `yolo11n.pt`.
- <strong>Object Segmentation</strong>: Model file: `yolo11n-seg.pt`.
- <strong>Pose Estimation</strong>: Model file: `yolo11n-pose.pt`.

### Implementation
- Built with <strong>Streamlit</strong> for a seamless user interface.
- Integrated <strong>Ultralytics YOLO</strong> for high-performance vision tasks.
- Supports both image and video input processing using OpenCV.

---

## Future Work

### Enhancements
- Add support for more vision models (e.g., YOLOv8, DETR).

### Expanded Input Types
- Support for additional video formats.

### Deployment
- Host the app on platforms like Hugging Face Spaces or Streamlit Cloud.

---

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request. If you encounter any issues, open a GitHub issue for discussion.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
