import cv2 as cv
from pathlib import Path

image_folder = Path(__file__).parents[1] / "data"
# cap = cv.VideoCapture(str(image_folder/"tree.avi"))
cap = cv.VideoCapture(0)
cap.set(3, 640) # width
cap.set(4, 480) # height
cap.set(10, 100) # brightness
# cehck the docs to see the other ids/variables

while True:
    exists, frame = cap.read()
    cv.imshow("Video", frame)
    if cv.waitKey(10) & 0xFF==ord('q'):
        break
