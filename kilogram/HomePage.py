import tkinter as tk

class HomePage(tk.Frame):
	def __init__(self,master) : 
		mainhomeframe = tk.Frame(master.navbar.midframe, bg = 'red')
		mainhomeframe.place(relheight = 1,relwidth = 1)