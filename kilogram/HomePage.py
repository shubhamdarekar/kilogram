import tkinter as tk

class HomePage(tk.Frame):
	def __init__(self,master) : 
		mainhomeframe = tk.Frame(master.navbar.midframe, bg = 'white')
		mainhomeframe.place(relheight = 1,relwidth = 1)

		self.usernamelabel = tk.Label(mainhomeframe,text = "hey",bg = 'black',fg = 'white',anchor = 'w',font=("Times", "13", "bold italic"))
		self.usernamelabel.place(relwidth = 0.8,relheight = 0.05,relx = 0.1,rely = 0.05)

		postframe = tk.Frame(mainhomeframe,bg = 'white')
		postframe.place(relheight =0.7,rely = 0.1,relwidth = 0.8,relx = 0.1 )

		self.postlabel = tk.Label(postframe)
		self.postlabel.place(relheight = 1,relwidth = 1)

		captionframe = tk.Frame(mainhomeframe,bg = 'black')
		captionframe.place(relheight = 0.08,rely = 0.8,relwidth=  0.8,relx = 0.1)

		self.captionlabel = tk.Label(captionframe,text ="hey",bg = 'black',fg = 'white',anchor = 'w',font=("Times", "13", "bold italic"))
		self.captionlabel.place(relx = 0.01,relwidth = 0.1)

		self.captionmsg = tk.Message(captionframe,bg = 'black',fg = 'white',anchor = 'w',text = 'akjhdkja skdhja hakjka oooau ahalnw lal ',width = 200)
		self.captionmsg.place(relx = 0.13,relheight = 1,relwidth = 0.4)

		buttonsframe = tk.Frame(mainhomeframe)
		buttonsframe.place(relx = 0.1,rely = 0.88,relheight = 0.07,relwidth = 0.8)

		self.nextbutton = tk.Button(buttonsframe,bg = 'black',text = 'Next' ,fg = 'White')
		self.nextbutton.place(relx = 0.5,relwidth = 0.5,relheight = 1)

		self.prevbutton = tk.Button(buttonsframe,bg = 'black',text = 'Previous' ,fg = 'White')
		self.prevbutton.place(relx = 0,relwidth = 0.5,relheight = 1)