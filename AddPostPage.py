import tkinter as tk

class AddPostPage(tk.Frame):
	def __init__(self,master):
		mainaddpostframe = tk.Frame(master.navbar.midframe, bg = 'pink')
		mainaddpostframe.place(relwidth = 1,relheight = 1)
		tk.Button(mainaddpostframe).pack()