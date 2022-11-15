import cv2 as cv
from pathlib import Path

image_folder = Path(__file__).parents[1] / "data"

img = cv.imread(str(image_folder/"lena.jpg"))
print(img.shape)

img_resize = cv.resize(img,(300,300))
print(img_resize.shape)

img_cropped = img[0:200,200:500]

cv.imshow("Image", img)
cv.imshow("Image resized",img_resize)
cv.imshow("Cropped Img",img_cropped)

cv.waitKey(0)