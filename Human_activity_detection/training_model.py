import cv2
import numpy as np
import mediapipe as mp
from keras.models import load_model
import csv
import time

# Initialize YOLOv8 for person detection
from ultralytics import YOLO
yolo_model = YOLO("yolov8n.pt")  # Load YOLOv8 pre-trained model for person detection

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Load the trained LSTM model
MODEL_PATH = "lstm_action_recognition_model.h5"  # Path to your trained LSTM model
model = load_model(MODEL_PATH)

# Labels for actions
LABELS = ["Clapping", "Meet", "Sitting", "Standing", "Walking"]  # Update with your action classes

# Function to extract keypoints from a single frame
def extract_keypoints(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)
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

    person_sequences = {}  # Store sequences for each person
    sequence_length = 30  # Same as training sequence length
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect persons using YOLO
        results = yolo_model(frame)
        detections = results[0].boxes.data.cpu().numpy()

        for i, detection in enumerate(detections):
            x1, y1, x2, y2, conf = map(int, detection[:5])
            if conf < 0.5:  # Confidence threshold
                continue

            # Crop person bounding box
            cropped_frame = frame[y1:y2, x1:x2]
            keypoints = extract_keypoints(cropped_frame)

            # Initialize a sequence for a new person ID
            if i not in person_sequences:
                person_sequences[i] = []

            person_sequences[i].append(keypoints)

            if len(person_sequences[i]) == sequence_length:
                input_data = np.expand_dims(person_sequences[i], axis=0)
                prediction = model.predict(input_data, verbose=0)
                confidence = np.max(prediction)
                action = LABELS[np.argmax(prediction)]

                # Annotate video with action for the person
                cv2.putText(frame, f"Person {i}: {action} ({confidence:.2f})",
                            (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                # Log to CSV
                timestamp = time.time() - start_time
                log_to_csv(csv_path, timestamp, i, action, confidence)

                # Maintain rolling sequence
                person_sequences[i].pop(0)

            # Draw bounding box and keypoints
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        out.write(frame)
        cv2.imshow("Video", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Example usage
SAMPLE_VIDEO = "input_video.mp4"  # Path to your input video
OUTPUT_VIDEO = "output_multi_person.mp4"  # Path to save the annotated output video
CSV_LOG_FILE = "action_log.csv"  # Path to save the CSV log file

process_video(SAMPLE_VIDEO, OUTPUT_VIDEO, CSV_LOG_FILE)
