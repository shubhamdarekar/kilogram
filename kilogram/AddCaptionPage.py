import tkinter as tk

class AddCaptionPage(tk.Frame):
	def __init__(self,master):
		mainframe = tk.Frame(master.navbar.midframe,bg = 'white')
		mainframe.place(relheight=1,relwidth = 1)

		self.imageframe = tk.Frame(mainframe)
		self.imageframe.place(relheight = 0.6,relwidth = 0.7 , relx = 0.15,rely=0.1)

		self.imagelabel = tk.Label(self.imageframe)
		self.imagelabel.place(relheight=1,relwidth=1)

		img =tk.PhotoImage(file = master.filepath)
		self.imagelabel.configure(image = img)

		label = tk.Label(mainframe,text = 'Add Caption:',bg = 'white',anchor = 'w')
		label.place(relwidth = 0.2,relheight = 0.05,relx = 0.15,rely = 0.7)
		
		self.captionbox = tk.Entry(mainframe,bg ='white')
		self.captionbox.place(relwidth = 0.7,relheight = 0.1,relx = 0.15,rely = 0.75)

		self.uploadbutton = tk.Button(mainframe,bg = 'black',text = 'Upload',fg = 'white',command = master.upload)
		self.uploadbutton.place(relwidth = 0.1 ,relheight = 0.07, relx = 0.8,rely = 0.9)

		
