import tkinter as tk
from tkinter import filedialog

class AddPostPage(tk.Frame):
	def __init__(self,master):
		mainaddpostframe = tk.Frame(master.navbar.midframe, bg = 'pink')
		mainaddpostframe.place(relwidth = 1,relheight = 1)
		fileuploadframe = tk.Frame(mainaddpostframe,bg='white')
		fileuploadframe.place(relheight = 0.1,relwidth = 1,rely = 0.9)
		self.addpostbutton = tk.Button(fileuploadframe,text = '+\nSelect Files',font = ('Ariel',10),command = master.pressaddpostbutton)
		self.addpostbutton.place(relheight = 0.8,relwidth = 0.16,relx = 0.4,rely = 0.1 )
