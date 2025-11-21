import cv2 as cv
import sys

img = cv.imread("image.jpg")

if img is None:
    sys.exit("file not found")

cv.imshow("image", img)
cv.waitKey()
cv.destroyWindow()

# pip install opencv-python
# = python3 -m pip install opencv-python