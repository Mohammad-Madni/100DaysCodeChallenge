from ultralytics import YOLO
import cv2
import numpy as np

# Loading YOLOv8n model which is given by Yolo
model = YOLO('yolov8n.pt')

# Defining labels for Mask detection
labels = ["No Mask", "Mask"]

# Initialization of webcam
cap = cv2.VideoCapture(0)

# for the real-time video process
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    # Extract detections
    for result in results:
        for box in result.boxes:
            # Extract bounding box coordinates and confidence
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = box.conf[0]
            class_id = box.cls[0]

            # Demo Mask detection
            label = labels[int(class_id % 2)]  # Alternate between Mask & No Mask for testing

            # Drawing bounding box and label
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display
    cv2.imshow("Face Mask Detection", frame)

    # 'q' key to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
