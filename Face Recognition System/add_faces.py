import os
import pickle

import cv2
import numpy as np

# Load face detection cascade
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Initialize video capture
video = cv2.VideoCapture(0)

# Initialize list to store faces and counter
faces_data = []
counter = 0

# Collect 100 images
while True:
    ret, frame = video.read()
    if not ret:
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    # Capture faces
    for (x, y, w, h) in faces:
        crop_img = cv2.resize(frame[y:y + h, x:x + w], (50, 50))  # Resize to 50x50
        faces_data.append(crop_img)
        counter += 1

        # Display the number of collected images
        cv2.putText(frame, str(counter), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)

    cv2.imshow("Frame", frame)

    # Break if 'q' is pressed or 100 images are collected
    if cv2.waitKey(1) & 0xFF == ord('q') or counter == 100:
        break

# Release video capture
video.release()
cv2.destroyAllWindows()

# Convert collected data to numpy array
faces_data = np.array(faces_data).reshape(-1, 50 * 50 * 3)

# Prompt user to enter their name
name = input("Enter Your Name: ")

# Load existing names data or create new if it doesn't exist
if os.path.exists('data/names.pkl'):
    with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
else:
    names = []

# Check if the user already exists
if name in names:
    print("User already exists.")
else:
    # Update names data
    names += [name] * counter

    # Save names data
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)

    # Load existing faces data or create new if it doesn't exist
    if os.path.exists('data/faces_data.pkl'):
        with open('data/faces_data.pkl', 'rb') as f:
            faces = pickle.load(f)
    else:
        faces = np.empty((0, 50 * 50 * 3))

    # Update faces data
    faces = np.vstack((faces, faces_data))

    # Save faces data
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces, f)

    print("Data saved successfully.")
