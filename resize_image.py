import cv2

img = cv2.imread('test.jpg')
img = cv2.resize(img, (225, 225))
cv2.imwrite('resized_test.jpg', img)