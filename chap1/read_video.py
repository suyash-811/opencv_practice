import cv2 as cv
from pathlib import Path

image_folder = Path(__file__).parents[1] / "data"
cap = cv.VideoCapture(str(image_folder/"tree.avi"))

while True:
    exists, frame = cap.read()