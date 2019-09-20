import tkinter as tk
import numpy as np
import cv2

class CameraPage(tk.Frame):
	def __init__(self,master):
		# maincameraframe = tk.Frame(master.navbar.midframe, bg = 'white')
		# maincameraframe.place(relwidth = 1,relheight = 1)
		cam = cv2.VideoCapture(0)

		cv2.namedWindow("Press Spacebar to capture the image.")

		self.flag = 1
		while True:
			ret, maincameraframe = cam.read()
			cv2.imshow("Press Spacebar to capture the image.", maincameraframe)
			if not ret:
				break
				
			k = cv2.waitKey(1)

			if k%256 == 27:
				self.flag = 0
				break
			elif k%256 == 32:
				img_name = "user.png"
				cv2.imwrite(img_name, maincameraframe)
				break

		cam.release()
		cv2.destroyAllWindows()



