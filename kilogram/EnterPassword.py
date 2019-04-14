import tkinter as tk

class EnterPassword(tk.Frame):
	def __init__(self,master):

		mainenterpassword_frame = tk.Frame(master.canvas,bg = "white")
		mainenterpassword_frame.place(relwidth = 1,relheight = 1)

		self.msg_label = tk.Label(mainenterpassword_frame,bg = "white",text = '')
		self.msg_label.place(relheight = 0.1,relwidth = 0.2,relx = 0.4,rely = 0.22)

		enterpassword_label = tk.Label(mainenterpassword_frame,bg = "white",fg = "black",text = "Enter Password",font = ('bold',20))
		enterpassword_label.place(relwidth = 0.5,relheight = 0.1,relx = 0.1,rely = 0.07)

		password_label = tk.Label(mainenterpassword_frame,bg = "white",fg = "black",text = "Password",font = ('bold',15))
		password_label.place(relheight = 0.1,relwidth = 0.3,relx = 0.285,rely = 0.37)

		self.enterpassword_entry = tk.Entry(mainenterpassword_frame,bg = "#ECECEC",show = "*")
		self.enterpassword_entry.place(relwidth = 0.1,relheight = 0.05,relx = 0.52,rely = 0.40)

		submit_button = tk.Button(mainenterpassword_frame,bg = "black",fg = "white",text = "Confirm",command = master.presschangepasswordbutton2)
		submit_button.place(relheight = 0.07,relwidth = 0.1,relx = 0.7,rely = 0.6)