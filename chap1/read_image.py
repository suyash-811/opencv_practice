import cv2 as cv
from pathlib import Path

print("Package Imported")
image_folder = Path(__file__).parents[1] / "data"
print(f"Image Folder: {image_folder}")


img = cv.imread(str(image_folder/"lena.jpg"))
cv.imshow("output",img)
cv.waitKey(0)