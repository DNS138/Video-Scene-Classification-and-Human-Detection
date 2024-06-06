# Video Scene Classification and Human Detection

This project classifies scenes in a video as either indoor or outdoor and detects the presence of people. The processed segments are saved in corresponding folders. The project includes a Streamlit application that allows users to upload a video and view the processed output.

## Project Directory Structure

Ensure your project directory has the following structure:

project_directory/
    ├── app.py
    ├── classifyScene.py
    ├── detectPeople.py
    ├── processSegments.py
    ├── res10_300x300_ssd_iter_140000.caffemodel
    ├── deploy.prototxt
    └── output/
        ├── indoor/
        ├── outdoor/
        ├── People_present/
        ├── People_not_present/

## Files Description

- `app.py`: The main Streamlit application script.
- `classify_scene.py`: Script for classifying scenes as indoor or outdoor using MobileNetV2.
- `detect_humans.py`: Script for detecting humans in the frame using a pre-trained Caffe model.
- `process_segments.py`: Script for saving video segments into the appropriate folders.
- `res10_300x300_ssd_iter_140000.caffemodel`: Pre-trained Caffe model file for human detection.
- `deploy.prototxt`: Prototxt file for the Caffe model.
- `output/`: Directory where the processed video segments are saved.

## Setup

### Prerequisites

- Python 3.x
- pip

### Packages

- streamlit
- openCV (cv2)
- TensorFlow
- numpy
- os

## Usage

1. Run the Streamlit application: `streamlit run app.py`
2. Upload a video file:
    Open a web browser and go to http://localhost:8501.
    Use the file uploader to upload a video file (mp4 or mov).
3. View the output:
    The application will process the video and save segments into the corresponding folders under the output directory:
    - output/indoor
    - output/outdoor
    - output/with_people
    - output/without_people
