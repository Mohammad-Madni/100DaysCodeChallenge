import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture('video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('pose_output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

movement_data = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    annotated_image = frame.copy()

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        movement_data.append([
            landmark.x for landmark in results.pose_landmarks.landmark
        ])

    out.write(annotated_image)
    cv2.imshow('Pose Estimation', annotated_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


plt.plot(np.mean(movement_data, axis=1))
plt.title('Movement Trends Over Time')
plt.xlabel('Frame Number')
plt.ylabel('Average X Position')
plt.show()
