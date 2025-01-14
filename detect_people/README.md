AI Vision Developer Assignment

This project detects people in a video using YOLOv8 and highlights them with bounding boxes and confidence scores. The processed video is saved for review.

Requirements
Python: Version 3.8 or higher.
PyCharm: For easy coding and running the project.
Dependencies: ultralytics (for YOLOv8)
opencv-python (for video processing)
torch
numpy

Steps to Set Up and Run
1. Download the Project
Download or clone this project and save it to your computer.
Example folder: C:/AI_Vision_Project.

2. Set Up PyCharm
Open PyCharm.
Click on File > Open, then select the project folder.
Go to File > Settings > Python Interpreter.
Add a new virtual environment: Click Add Interpreter > New Virtual Environment.
Click OK to create it.

3. Install Required Packages
Open the Terminal in PyCharm (bottom of the screen).
Run this command:
bash
Copy code
pip install ultralytics opencv-python torch numpy

4. Prepare Files
Place your trained YOLO model file (best.pt) in the weights folder (create it if it doesn't exist).
Save the video you want to process as input.mp4 in the project folder.

5. Run the Code
Open main.py in PyCharm.
Click the Run button (green triangle at the top-right of PyCharm).
The processed video will be saved as output.mp4 in the project folder.
How to Use the Script
Change the model file: If you have a different model file, update this line in main.py:
python
Copy code
model = YOLO('weights/best.pt')
Change the input video: Replace 'input.mp4' with the name of your video file.

Expected Output
A new video file, output.mp4, with bounding boxes around detected people and their confidence scores.
