import cv2
import numpy as np
import mediapipe as mp
from keras.models import load_model
import csv
import time

# Initializing MediaPipe Pose Estimation Model
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Loading the trained LSTM model which i trained using dataset from kaggle
MODEL_PATH = "lstm_action_recognition_model.h5"
model = load_model(MODEL_PATH)

# Labels for actions recognition
LABELS = ["Clapping", "Meet", "Sitting", "Standing", "Walking"]

# Function to extract keypoints from a single frame
def extract_keypoints(results):
    if results.pose_landmarks:
        keypoints = np.array([[lm.x, lm.y, lm.z] for lm in results.pose_landmarks.landmark]).flatten()
    else:
        keypoints = np.zeros(99)  # Placeholder for missing keypoints
    return keypoints

# Function to log actions to a CSV file
def log_to_csv(csv_path, timestamp, person_id, action, confidence):
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, person_id, action, confidence])

# Function to process video and detect multi-person actions
def process_video(video_path, output_path, csv_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Prepare CSV logging
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Person_ID", "Action", "Confidence"])

    sequences = {}  # Store sequences for each person
    person_ids = [1, 2]  # Assuming only two persons
    sequence_length = 30  # Same as training sequence length

    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb_frame)

        # Multi-person handling (MediaPipe doesn't natively track multiple persons, so we'll simulate it here)
        keypoints = extract_keypoints(results)

        for person_id in person_ids:
            if person_id not in sequences:
                sequences[person_id] = []

            sequences[person_id].append(keypoints)

            if len(sequences[person_id]) == sequence_length:
                input_data = np.expand_dims(sequences[person_id], axis=0)
                prediction = model.predict(input_data, verbose=0)
                confidence = np.max(prediction)
                action = LABELS[np.argmax(prediction)]

                # Annotate video with action for the person
                y_position = 50 + 50 * person_id  # Adjust Y-position for each person
                cv2.putText(frame, f"Person {person_id}: {action} ({confidence:.2f})",
                            (10, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                # Log to CSV
                timestamp = time.time() - start_time
                log_to_csv(csv_path, timestamp, person_id, action, confidence)

                # Maintaining the rolling sequence
                sequences[person_id].pop(0)

        # Draw pose landmarks
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        out.write(frame)
        cv2.imshow("Video", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Usage
SAMPLE_VIDEO = "input_video.mp4"  # Path to your input video
OUTPUT_VIDEO = "output_multi_person.mp4"
CSV_LOG_FILE = "actions_log.csv"

process_video(SAMPLE_VIDEO, OUTPUT_VIDEO, CSV_LOG_FILE)