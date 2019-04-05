import tkinter as tk

class ChangeUsername(tk.Frame):
	def __init__(self,master):
		
		mainchangeusername_frame = tk.Frame(master.editprofile.maineditprofile_frame,bg = "white")
		mainchangeusername_frame.place(relheight = 1,relwidth = 1)

		back_button = tk.Button(mainchangeusername_frame,bg = "black",fg = "white",text = "Back",command = master.presseditprofilebutton)
		back_button.place(relheight = 0.07,relwidth = 0.1,relx = 0.1,rely = 0.07)

		main_label = tk.Label(mainchangeusername_frame,bg = "white",text = "Change Username",font = ('bold',20))
		main_label.place(relheight = 0.1,relwidth = 0.5,relx = 0.25,rely = 0.05)

		oldusername_label = tk.Label(mainchangeusername_frame,bg = "white",text = "Old Username",font = ('bold',15))
		oldusername_label.place(relheight = 0.1,relwidth = 0.3,relx = 0.25,rely = 0.25)

		self.oldusername_label1 = tk.Label(mainchangeusername_frame,bg = "#ECECEC",text = master.username,font = 20)
		self.oldusername_label1.place(relheight = 0.05,relwidth = 0.1,relx = 0.55,rely = 0.28)

		newusername_label = tk.Label(mainchangeusername_frame,bg = "white",text = "New Username",font = ('bold',15))
		newusername_label.place(relheight = 0.1,relwidth = 0.3,relx = 0.25,rely = 0.35)

		self.newusername_entry = tk.Entry(mainchangeusername_frame,bg = "#ECECEC")
		self.newusername_entry.place(relheight = 0.05,relwidth = 0.1,relx = 0.55,rely = 0.38)

		submit_button = tk.Button(mainchangeusername_frame,bg = "black",fg = "white",text = "Confirm",command = master.presschangeusernamebutton1)
		submit_button.place(relheight = 0.07,relwidth = 0.1,relx = 0.7,rely = 0.6)