import cv2

frameWidth = 640
frameHight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHight)
cap.set(10,130)


while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
