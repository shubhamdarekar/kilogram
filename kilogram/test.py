import numpy as np
import urllib.request
import cv2
from skimage import io
image = io.imread('https://firebasestorage.googleapis.com/v0/b/kilogramlikeinstagram.appspot.com/o/images%2Fnew1.jpg?alt=media')
# with urllib.request.urlopen('https://firebasestorage.googleapis.com/v0/b/kilogramlikeinstagram.appspot.com/o/images%2Fnew1.jpg?alt=media') as url:
# 	resp = url.read()
# image = np.asarray(bytearray(resp.read()), dtype="uint8")
# image = cv2.imdecode(image, cv2.IMREAD_COLOR)

cv2.imshow('image',image)
cv2.waitKey(0)
