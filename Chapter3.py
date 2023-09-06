import cv2
import numpy as np

img = cv2.imread("resource1/us.jpg")

cv2.imshow("Image",img)
print(img.shape)

imgResize = cv2.resize(img,(400,600))
print(imgResize.shape)

#imgCropped = img[0:20,300:500]

cv2.imshow("Images",img)
cv2.imshow("Images Resize",imgResize)
#cv2.imshow("Images Cropped",imgCropped)

cv2.waitKey(0)