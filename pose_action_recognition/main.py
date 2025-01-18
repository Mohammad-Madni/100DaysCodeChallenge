import cv2
import mediapipe as mp
import numpy as np
import csv
from datetime import datetime
from keras.models import load_model
import tensorflow as tf

# Fix optimizer configuration if required
from keras.optimizers import Adam

# Save the original `from_config` method
original_from_config = tf.keras.optimizers.Adam.from_config

# Define the custom optimizer function
def custom_optimizer(config):
    if "lr" in config:  # Rename "lr" to "learning_rate" if found
        config["learning_rate"] = config.pop("lr")
    return original_from_config(config)  # Use the original method

# Replace the `from_config` method with the custom function
tf.keras.optimizers.Adam.from_config = custom_optimizer

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Load the model
action_model = load_model('action_recognition_model.h5')

# Define possible actions
actions = ['standing', 'walking', 'sitting', 'jumping']

# Initialize CSV for logging
with open('actions_log.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Timestamp', 'Action', 'Confidence'])

    # Video Input and Output
    cap = cv2.VideoCapture('input_video.mp4')
    out = cv2.VideoWriter('action_output.mp4', cv2.VideoWriter_fourcc(*'mp4v'),
                          int(cap.get(cv2.CAP_PROP_FPS)),
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    sequence = []
    sequence_length = 30

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process Frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(rgb_frame)

        if result.pose_landmarks:
            # Extract and flatten the first 26 pose keypoints (x, y, z)
            keypoints = np.array([[lm.x, lm.y, lm.z] for lm in result.pose_landmarks.landmark])[:26]  # First 26 landmarks
            keypoints = keypoints.flatten()  # Flatten to match the model input shape
            sequence.append(keypoints)

            if len(sequence) == sequence_length:
                # Predict Action
                prediction = action_model.predict(np.expand_dims(sequence, axis=0), verbose=0)
                confidence = np.max(prediction)
                action = actions[np.argmax(prediction)]

                # Log Data
                csv_writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), action, confidence])

                # Display Action on Frame
                cv2.putText(frame, f'{action} ({confidence:.2f})', (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Pop the first element to maintain sequence length
                sequence.pop(0)

        # Write the processed frame with prediction
        out.write(frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()

cv2.destroyAllWindows()
