import tkinter as tk

class EditProfile(tk.Frame):
	def __init__(self,master):

		self.maineditprofile_frame = tk.Frame(master.canvas,bg = "white")
		self.maineditprofile_frame.place(relheight = 1,relwidth = 1)

		back_button = tk.Button(self.maineditprofile_frame,bg = "black",fg = "white",text = "Back",command = master.pressmyprofilebutton)
		back_button.place(relheight = 0.07,relwidth = 0.1,relx = 0.1,rely = 0.07)

		self.usernamechangesuccessful_label = tk.Label(self.maineditprofile_frame,bg = "white",text = '',font = ('bold',10))
		self.usernamechangesuccessful_label.place(relheight = 0.1,relwidth = 0.4,relx = 0.2,rely = 0.15)

		mainlabel = tk.Label(self.maineditprofile_frame,bg = "white",text = "Edit Profile",font = ('bold',30))
		mainlabel.place(relheight = 0.1,relwidth = 0.4,relx = 0.3,rely = 0.05)

		changeusername_button = tk.Button(self.maineditprofile_frame,bg = "black",fg = "white",text = "Change Username",font = ('bold',20),command = master.presschangeusernamebutton)
		changeusername_button.place(relheight = 0.1,relwidth = 0.8,relx = 0.1,rely = 0.25)

		changepassword_button = tk.Button(self.maineditprofile_frame,bg = "black",fg = "white",text = "Change Password",font = ('bold',20),command = master.presschangepasswordbutton)
		changepassword_button.place(relheight = 0.1,relwidth = 0.8,relx = 0.1,rely = 0.40)

		changeprofilepicture_button = tk.Button(self.maineditprofile_frame,bg = "black",fg = "white",text = "Change Profile Picture",font = ('bold',20),command = master.presschangeprofilepicturebutton)
		changeprofilepicture_button.place(relheight = 0.1,relwidth = 0.8,relx = 0.1,rely = 0.55)

