import tkinter as tk

class NotificationsPage(tk.Frame):
	def __init__(self,master):
		mainnotificationframe = tk.Frame(master.navbar.midframe, bg = 'white')
		mainnotificationframe.place(relwidth = 1,relheight = 1)
		self.following_frame = tk.Frame(mainnotificationframe,bg = "white")
		self.following_frame.place(relheight = 0.5,relwidth = 0.33)

		self.followed_frame = tk.Frame(mainnotificationframe,bg = "white")
		self.followed_frame.place(relheight = 0.5,relwidth = 0.33,rely = 0.5)

		self.post_frame = tk.Frame(mainnotificationframe,bg = "white")
		self.post_frame.place(relheight = 1,relwidth = 0.33,relx = 0.33)
		
		self.message_frame = tk.Frame(mainnotificationframe,bg = "white")
		self.message_frame.place(relheight = 1,relwidth = 0.34,relx = 0.66)