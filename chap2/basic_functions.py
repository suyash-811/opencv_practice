import cv2 as cv
import numpy as np
from pathlib import Path

image_folder = Path(__file__).parents[1] / "data"

img = cv.imread(str(image_folder/"lena.jpg"))
print(type(img))

# convert to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img_gray,(7,7),0)
img_canny = cv.Canny(img,100,100)
kernel = np.ones((5,5),np.uint8)
img_dilation = cv.dilate(img_canny,kernel=kernel,iterations=1)
img_eroded = cv.erode(img_dilation,kernel,iterations=1)

cv.imshow("Gray Image", img_gray)
cv.imshow("Blur Image", img_blur)
cv.imshow("Canny Image", img_canny)
cv.imshow("Dilation Image", img_dilation)
cv.imshow("Eroded Image", img_eroded)
cv.waitKey(0)
