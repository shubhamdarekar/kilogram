import tkinter as tk
import cv2

class CameraPage(tk.Frame):
	def __init__(self,master):
		maincameraframe = tk.Frame(master.navbar.midframe, bg = 'blue')
		maincameraframe.place(relwidth = 1,relheight = 1)
		cam = cv2.VideoCapture(0)

		cv2.namedWindow("Camera Window")

		img_counter = 0

		while True:
			ret, maincameraframe = cam.read()
			cv2.imshow("Camera Window", maincameraframe)
			if not ret:
				break
				k = cv2.waitKey(1)

			if k%256 == 27:
				print("You Escaped.")
				break
			elif k%256 == 32:
				img_name = "opencv_frame_{}.png".format(img_counter)
				cv2.imwrite(img_name, frame)
				print("{} written!".format(img_name))
				print("Image Captured.")
				img_counter += 1
		cam.release()
		cv2.destroyAllWindows()



