import tkinter
import cv2
from tkinter import filedialog

# Hides the root of tkinter
root = tkinter.Tk()
root.withdraw()

# Load the cascade
face_cascade = cv2.CascadeClassifier('./templates/haarcascade_frontalface_default.xml')

# Ask the user for image input
filepath = filedialog.askopenfilename()

# Read the input image
img = cv2.imread(filepath)

# Convert the image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
if faces.any() == True:
    print("FOUND A FACE!!")

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()