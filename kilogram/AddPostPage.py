import tkinter as tk
from tkinter import filedialog

class AddPostPage(tk.Frame):
	def __init__(self,master):
		mainaddpostframe = tk.Frame(master.navbar.midframe, bg = 'white')
		mainaddpostframe.place(relwidth = 1,relheight = 1)

		fileuploadframe = tk.Frame(mainaddpostframe,bg='gray')
		fileuploadframe.place(relheight = 0.1,relwidth = 1,rely = 0.9)

		# self.fileuploadempty = tk.Label() 

		self.addpostbutton = tk.Button(fileuploadframe,text = '+\nSelect Files',font = ('Ariel',10),command = master.pressaddpostbutton1)
		self.addpostbutton.place(relheight = 0.8,relwidth = 0.16,relx = 0.4,rely = 0.1 )

		self.filelabel = tk.Label(mainaddpostframe,bg='white')
		self.filelabel.place(relheight = 0.9,relwidth = 1,rely = 0)

		# self.newlabel = tk.Canvas(self.filelabel,width = 700,height = 700,bg='red')
		# self.newlabel.pack()
		self.captionbutton = tk.Button(fileuploadframe,text = 'Next',bg='black',fg='white',font = ('Ariel',10),command = master.pressnextbutton)
		self.captionbutton.place(relheight = 0.8,relwidth = 0.1 ,relx = 0.8 ,rely = 0.1)


	# def pressaddpostbutton1(self):
	# 	self.filepath = filedialog.askopenfilename()
	# 	print(self.filepath)
	# 	#self.addpostpage = AddPostPage.AddPostPage(self)
	# 	img =tk.PhotoImage(file = self.filepath)
	# 	print(img)
	# 	# self.newlabel.create_image(20,20,anchor = 'nw',image = img)
	# 	self.filelabel.configure(image = img)
	# 	master.mainloop()
