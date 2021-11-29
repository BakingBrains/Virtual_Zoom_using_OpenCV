import cv2
from cvzone.HandTrackingModule import HandDetector

# Input from webcam
frame = cv2.VideoCapture(0)
frame.set(3, 1280)
frame.set(4, 720)

# initialize hand detector module with some confidence
handDetector = HandDetector(detectionCon=0.8)

# loop
while True:
    # Read the frames from webcam
    res, img = frame.read()

    # detect the hands, by default it will detect two hands
    hands = handDetector.findHands(img)

    # show the output
    cv2.imshow("Sample CVZone output", img)
    cv2.waitKey(1)
