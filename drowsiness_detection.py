import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    brightness = np.mean(gray)

    if brightness < 50:
        print("Drowsiness Detected!")

    cv2.imshow("Drowsiness Monitor", frame)

    if cv2.waitKey(1) == 27:
        break