import tkinter as tk

class Lowernavbar:
	def __init__(self,master):
		# global screen1
		# global lowernavbarframe
		# global homebutton
		# global searchbutton
		# global addpostbutton
		# global notificationsbutton
		# global profilebutton

		screen1 = tk.Frame(master.canvas,bg="white")
		screen1.place(relheight = 1,relwidth = 1)
		
		uppernavbarframe = tk.Frame(screen1,bg = "black")
		uppernavbarframe.place(relheight = 0.075,relwidth = 1)

		title_label = tk.Label(uppernavbarframe , anchor = 'center',text = "Kilogram",fg = "white",height=55,bg="black",font = ('Zefani',35))
		title_label.place(relwidth = 0.3,relheight = 0.98 ,relx = 0.32,rely = 0.01)

		messagebutton = tk.Button(uppernavbarframe,text = 'DM',bg = 'white')
		messagebutton.place(relwidth = 0.075,relheight = 0.7,relx = 0.915,rely=0.15)

		camerabutton = tk.Button(uppernavbarframe,text = 'Camera',bg = 'white',height=2,width=20)
		camerabutton.place(relwidth = 0.075,relheight = 0.7,relx=0.01,rely = 0.15)


		lowernavbarframe = tk.Frame(screen1,bg = "black")
		lowernavbarframe.place(relheight = 0.05,relwidth = 1,rely = 0.95)

		homebutton = tk.Button(lowernavbarframe,text = "Home",bg= "white",height = 2,width = 30)
		homebutton.grid(row = 0 ,column = 0)

		searchbutton = tk.Button(lowernavbarframe,text = "Search",bg= "white",height = 2,width = 30)
		searchbutton.grid(row = 0 ,column = 1)

		addpostbutton = tk.Button(lowernavbarframe,text = "Add Post",bg= "white",height = 2,width = 29)
		addpostbutton.grid(row = 0 ,column = 2,padx = 1)

		notificationsbutton = tk.Button(lowernavbarframe,text = "Notifications",bg= "white",height = 2,width = 29)
		notificationsbutton.grid(row = 0 ,column = 3)

		profilebutton = tk.Button(lowernavbarframe,text = "My Profile",bg= "white",height = 2,width = 30)
		profilebutton.grid(row = 0 ,column = 4)

