import cv2
from cvzone.HandTrackingModule import HandDetector

# Input from webcam
frame = cv2.VideoCapture(0)
frame.set(3, 1280)
frame.set(4, 720)

# initialize hand detector module
handDetector = HandDetector(detectionCon=0.8)
distStart = None
zoom_range = 0
cx, cy = 500, 500

# loop
while True:
    # Read the input frame
    res, img = frame.read()

    # Detect the hands
    hands, img = handDetector.findHands(img)

    # Image to be zoomed
    new_img = cv2.imread('resized_test.jpg')

    # if two hands are detected
    if len(hands) == 2:
        # print("Start Zoom...")
        # print(handDetector.fingersUp(hands[0]))
        # print(handDetector.fingersUp(hands[1]))

        #
        if handDetector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and handDetector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            # print("Start Zoom...")
            lmList1 = hands[0]['lmList']
            lmList2 = hands[1]['lmList']

            # point 8 is tip of the index finger
            if distStart is None:
                # length, info, img = handDetector.findDistance(lmList1[8], lmList2[8], img)
                # draw the connection points between right hand index and thum finger to left hand
                length, info, img = handDetector.findDistance(hands[0]['center'], hands[1]['center'], img)
                # print(length)
                distStart = length

            # length, info, img = handDetector.findDistance(lmList1[8], lmList2[8], img)
            length, info, img = handDetector.findDistance(hands[0]['center'], hands[1]['center'], img)
            # info gives center x and center y
            # calculate the zoom range
            zoom_range = int((length - distStart) // 2)
            # calculate the center point so that we can  place the zooming image at the center
            cx, cy = info[4:]
            print(zoom_range)

    else:
        distStart = None

    try:
        h, w, _ = new_img.shape

        # new height and new width
        newH, newW = ((h + zoom_range) // 2) * 2, ((w + zoom_range) // 2) * 2
        new_img = cv2.resize(new_img, (newW, newH))

        # we want the zooming image to be center and place it approx at the center
        img[cy - newH // 2:cy + newH // 2, cx - newW // 2:cx + newW // 2] = new_img

    except:
        pass

    # display output
    cv2.imshow('output', img)
    cv2.waitKey(1)
