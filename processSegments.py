import cv2
import os

# Function to save segment
def save_segment(video_path, output_dir, start_frame, end_frame, category, fps):
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    output_dirs = category.split('_', 2)[0:2]

    if output_dirs[1] == 'with':
      output_dirs[1] = 'People_present'
    else:
      output_dirs[1] = 'People_not_present'


    # Iterate over each output directory
    for x in output_dirs:
        # Create the output directory if it doesn't exist
        os.makedirs(os.path.join(output_dir, x), exist_ok=True)

        # Create a video writer for the current output directory
        out = cv2.VideoWriter(os.path.join(output_dir,x , f"{x}_{start_frame}_{end_frame}.mp4"), fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

        # Write each frame of the segment to the video file
        for _ in range(start_frame, end_frame):
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

        # Release the video writer
        out.release()

    # Release the video capture
    cap.release()
