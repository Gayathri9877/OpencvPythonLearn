import cv2
print("package imported")

img = cv2.imread("resource1/img.png")
cv2.imshow("output",img)
cv2.waitKey(0)
