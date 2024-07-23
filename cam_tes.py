import cv2
import os
import time
import glob

# Define the folder to save frames
save_folder = 'captured_frames'

# Ensure the save folder exists and is empty
if os.path.exists(save_folder):
    files = glob.glob(os.path.join(save_folder, '*'))
    for f in files:
        os.remove(f)
else:
    os.makedirs(save_folder)

# Initialize the camera
cap = cv2.VideoCapture(2)  # 0 is the default camera, change if necessary

if not cap.isOpened():
    print("Error: Could not open video capture")
    exit()

# Frame rate
fps = 20
frame_count = 0

try:
    while True:
        start_time = time.time()

        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Save the captured frame
        frame_filename = os.path.join(save_folder, f'frame_{frame_count:04d}.png')
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

        # Calculate sleep time to maintain 10 FPS
        elapsed_time = time.time() - start_time
        sleep_time = max(1.0 / fps - elapsed_time, 0)
        time.sleep(sleep_time)

        # Break loop after capturing the desired number of frames (optional)
        if frame_count >= 20:  # Example: stop after 100 frames
            break

finally:
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

print(f"Captured {frame_count} frames at {fps} FPS")
