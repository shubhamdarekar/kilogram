import numpy
import cv2

cam = cv2.videoCapture(0)

while True:
	ret,b = cam.read()
	cv2.imshow('kilogram',b)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break
b.release()
cv2.destroyAllWindows