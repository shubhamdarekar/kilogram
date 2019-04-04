import tkinter as tk

class NotificationsPage(tk.Frame):
	def __init__(self,master):
		mainnotificationframe = tk.Frame(master.navbar.midframe, bg = 'yellow')
		mainnotificationframe.place(relwidth = 1,relheight = 1)
		notifications_frame = tk.Frame(mainnotificationframe,bg = "white")
		notifications_frame.place(relwidth = 0.7,relx = 0.15,relheight = 0.8,rely = 0.1)
		notifications_label = tk.Label(notifications_frame,text = "Your Notifications",bg = "white")
		notifications_label.place(relx = 0.2,rely = 0.2)