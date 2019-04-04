import tkinter as tk
from Root import *
def lower_navbar():
	global screen1
	global navbar_frame
	screen1 = tk.Frame(canvas,bg="white")
	screen1.place(relheight = 1,relwidth = 1)

	navbarframe = tk.Frame(screen1,height = 70, width = 1080,bg = "black")
	navbarframe.pack(side= 'bottom')

	home_button = tk.Button(navbarframe,text = "Home",bg= "white",height = 40,width = 180,pady = 15,padx = 30)
	home_button.place()

	root.mainloop()

lower_navbar()