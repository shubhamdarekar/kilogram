import tkinter as tk

class SearchPage(tk.Frame):
	def __init__(self,master):
		mainsearchframe = tk.Frame(master.navbar.midframe, bg = 'blue')
		mainsearchframe.place(relwidth = 1,relheight = 1)
