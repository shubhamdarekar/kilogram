import tkinter as tk
class ChangePassword(tk.Frame):
 	def __init__(self,master):

 		mainchangepassword_frame = tk.Frame(master.canvas,bg = "white")
 		mainchangepassword_frame.place(relwidth = 1,relheight = 1)

 		self.changepasswordunsuccessful_label = tk.Label(mainchangepassword_frame,bg = "white",text = "")
 		self.changepasswordunsuccessful_label.place(relheight = 0.1,relwidth = 0.2,relx = 0.4,rely = 0.12)

 		back_button = tk.Button(mainchangepassword_frame,bg = "black",fg = "white",text = "Back",command = master.presseditprofilebutton)
 		back_button.place(relheight = 0.07,relwidth = 0.1,relx = 0.1,rely = 0.07)

 		main_label = tk.Label(mainchangepassword_frame,bg = "white",text = "Change Password",font = ('bold',20))
 		main_label.place(relheight = 0.1,relwidth = 0.5,relx = 0.25,rely = 0.05)

 		newpassword_label = tk.Label(mainchangepassword_frame,bg = "white",text = "New Password",font = ('bold',15))
 		newpassword_label.place(relheight = 0.1,relwidth = 0.3,relx = 0.25,rely = 0.25)

 		self.newpassword_entry = tk.Entry(mainchangepassword_frame,bg = "#ECECEC",show = "*")
 		self.newpassword_entry.place(relheight = 0.05,relwidth = 0.1,relx = 0.55,rely = 0.25)

 		confirmpassword_label = tk.Label(mainchangepassword_frame,bg = "white",text = "Confirm Password",font = ('bold',15))
 		confirmpassword_label.place(relheight = 0.1,relwidth = 0.3,relx = 0.25,rely = 0.35)

 		self.confirmpassword_entry = tk.Entry(mainchangepassword_frame,bg = "#ECECEC",show = "*")
 		self.confirmpassword_entry.place(relheight = 0.05,relwidth = 0.1,relx = 0.55,rely = 0.38)

 		submit_button = tk.Button(mainchangepassword_frame,bg = "black",fg = "white",text = "Confirm",command = master.presschangepasswordbutton1)
 		submit_button.place(relheight = 0.07,relwidth = 0.1,relx = 0.7,rely = 0.6)