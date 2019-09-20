import tkinter as tk
from skimage import io
import urllib
import cv2
from PIL import ImageTk, Image

class HomePage(tk.Frame):
	def __init__(self,master) : 
		

		image = io.imread('https://firebasestorage.googleapis.com/v0/b/kilogramlikeinstagram.appspot.com/o/uiimages%2Fkilo.png?alt=media&token=114fabd9-dc0c-47c7-bb83-da8302ad07f1')
		image = cv2.resize(image, (400,250), interpolation = cv2.INTER_AREA)
		image = Image.fromarray(image)
		image = ImageTk.PhotoImage(image)

		mainhomeframe = tk.Canvas(master.navbar.midframe, bg = 'white')
		mainhomeframe.place(relheight = 1,relwidth = 1)


		mainhomeframe.create_image(0,0,image = image)

		# l1 = tk.Label(mainhomeframe,image= image)
		# l1.place (relheight=  1,relwidth = 1)

		# l1.image = image

		self.usernamelabel = tk.Label(mainhomeframe,text = "",bg = 'black',fg = 'white',anchor = 'w',font=("Times", "13", "bold italic"))
		self.usernamelabel.place(relwidth = 0.8,relheight = 0.05,relx = 0.1,rely = 0.05)

		postframe = tk.Frame(mainhomeframe,bg = 'white')
		postframe.place(relheight =0.7,rely = 0.1,relwidth = 0.8,relx = 0.1 )

		self.postlabel = tk.Label(postframe)
		self.postlabel.place(relheight = 1,relwidth = 1)

		captionframe = tk.Frame(mainhomeframe,bg = 'black')
		captionframe.place(relheight = 0.08,rely = 0.8,relwidth=  0.8,relx = 0.1)

		self.captionlabel = tk.Label(captionframe,text ="",bg = 'black',fg = 'white',anchor = 'w',font=("Times", "13", "bold italic"))
		self.captionlabel.place(relx = 0.01,relwidth = 0.18)

		self.captionmsg = tk.Message(captionframe,bg = 'black',fg = 'white',anchor = 'w',text = '',width = 200)
		self.captionmsg.place(relx = 0.13,relheight = 1,relwidth = 0.4)

		buttonsframe = tk.Frame(mainhomeframe)
		buttonsframe.place(relx = 0.1,rely = 0.88,relheight = 0.07,relwidth = 0.8)

		self.nextbutton = tk.Button(buttonsframe,bg = 'black',text = 'Next' ,fg = 'White',command = master.nextbutton1)
		self.nextbutton.place(relx = 0.5,relwidth = 0.5,relheight = 1)

		self.prevbutton = tk.Button(buttonsframe,bg = 'black',text = 'Previous' ,fg = 'White',command = master.prevbutton1)
		self.prevbutton.place(relx = 0,relwidth = 0.5,relheight = 1)