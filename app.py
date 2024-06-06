import streamlit as st
import cv2
import os
from classifyScene import classify_scene
from detectPeople import detect_people
from processSegments import save_segment

def process_video(video_path, output_dir):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    output_dirs = []

    current_segment = None
    segment_start_frame = 0

    for frame_num in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        scene_type = classify_scene(frame)
        people_present = detect_people(frame)

        category = f"{scene_type}_with_people" if people_present else f"{scene_type}_without_people"

        if current_segment is None:
            current_segment = category
            segment_start_frame = frame_num
        elif category != current_segment:
            segment_end_frame = frame_num
            save_segment(video_path, output_dir, segment_start_frame, segment_end_frame, current_segment, fps)
            current_segment = category
            segment_start_frame = frame_num

    # Save the last segment
    if current_segment is not None:
        segment_end_frame = frame_count - 1
        save_segment(video_path, output_dir, segment_start_frame, segment_end_frame, current_segment, fps)

    cap.release()

st.title("Video Processing Application")

# Upload video file
uploaded_file = st.file_uploader("Upload Video File", type=["mp4", "mov"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    temp_video_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(temp_video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display video
    st.video(temp_video_path)

    # Process video and save into folders
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    process_video(temp_video_path, output_dir)

    st.write("Video processed and saved into the following folders:")
    st.write("Indoor Scenes Folder:", os.path.join(output_dir, "indoor"))
    st.write("Outdoor Scenes Folder:", os.path.join(output_dir, "outdoor"))
    st.write("Scenes with People Folder:", os.path.join(output_dir, "with_people"))
    st.write("Scenes without People Folder:", os.path.join(output_dir, "without_people"))

    # Clean up the temporary video file
    os.remove(temp_video_path)
