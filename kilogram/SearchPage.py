import tkinter as tk

class SearchPage(tk.Frame):
	def __init__(self,master):
		mainsearchframe = tk.Frame(master.navbar.midframe, bg = 'blue')
		mainsearchframe.place(relwidth = 1,relheight = 1)

		searchpage_frame = tk.Frame(mainsearchframe,bg = "white")
		searchpage_frame.place(relwidth = 1,relheight = 1)

		self.search_label = tk.Label(searchpage_frame,bg = "white",text = "Search",font = 30)
		self.search_label.place(relwidth = 0.1,relheight = 0.07,relx = 0.2,rely = 0.05)

		self.search_entry = tk.Entry(searchpage_frame,bg = "#ECECEC")
		self.search_entry.place(relwidth = 0.38, relheight = 0.04,relx = 0.3,rely = 0.07)

		self.search_button = tk.Button(searchpage_frame,bg = "black",fg = "white",text = "Search",command = master.presssearchbutton1)
		self.search_button.place(relwidth = 0.1,relheight = 0.04,relx = 0.7,rely= 0.067)

		self.frame = tk.Frame(searchpage_frame,bg = "white")
		self.frame.place(relheight = 0.8,relwidth = 0.6,relx = 0.2,rely = 0.15)

		
		# self.searches = tk.Message(searchpage_frame,text = '')
		# self.searches.pack()