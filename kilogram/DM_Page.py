import tkinter as tk

class DM_Page(tk.Frame):
	def __init__(self,master):
		self.mainDMframe = tk.Frame(master.navbar.midframe, bg = 'white')
		self.mainDMframe.place(relwidth = 1,relheight = 1)

		self.searchuser_label = tk.Label(self.mainDMframe,bg = "white",text = "Find User",font = ('Ariel', 15))
		self.searchuser_label.place(relwidth = 0.1,relheight = 0.04,relx = 0.2,rely = 0.03)

		self.searchuser_entry = tk.Entry(self.mainDMframe,bg = "#ECECEC")
		self.searchuser_entry.place(relwidth = 0.35, relheight = 0.04,relx = 0.32,rely = 0.03)

		self.searchuser_button = tk.Button(self.mainDMframe,bg = "white",text = "Search", command = master.presssearchbutton3)
		self.searchuser_button.place(relwidth = 0.1,relheight = 0.04,relx = 0.7,rely= 0.03)

		self.frame = tk.Frame(self.mainDMframe,bg = "white")
		self.frame.place(relheight = 0.8,relwidth = 0.6,relx = 0.2,rely = 0.15)
		
	def openframe(self):
		messageframe = tk.Frame(self.mainDMframe, bg = 'red')
		messageframe.place(relwidth=1, relheight=1)