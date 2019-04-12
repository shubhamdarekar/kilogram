import tkinter as tk 

class MyProfilePage(tk.Frame):
	def __init__(self,master):
		mainprofileframe = tk.Frame(master.navbar.midframe,bg = 'white')
		mainprofileframe.place(relheight = '1',relwidth = 1)

		# myprofilelabel=tk.Label(mainprofileframe, text="My Profile", bg='pink', font=('bold'))
		# myprofilelabel.place(relx=0.44,rely=0.03, relwidth=0.3, relheight=0.045)

		imagelabel=tk.Label(mainprofileframe)
		imagelabel.place(relx=0.22,rely=0.05,relwidth=0.15, relheight=0.18)

		self.username1label=tk.Label(mainprofileframe,bg = 'white',font = ('Ariel',25))
		self.username1label.place(relx=0.22,rely=0.23,relwidth=0.15, relheight=0.055)

		self.postnumber = tk.Label(mainprofileframe,text = '0',bg = 'white',font = ('Ariel',30) )
		self.postnumber.place(relx = 0.44,rely = 0.09)

		postslabel=tk.Label(mainprofileframe, text="Posts", bg='white', font=('bold'))
		postslabel.place(relx=0.4,rely=0.16, relwidth=0.1, relheight=0.045)

		self.followernumber = tk.Label(mainprofileframe,text = '0',bg = 'white',font = ('Ariel',30) )
		self.followernumber.place(relx = 0.58,rely = 0.09)

		followerslabel=tk.Label(mainprofileframe, text="Followers", bg='white', font=('bold'))
		followerslabel.place(relx=0.54,rely=0.16, relwidth=0.1, relheight=0.045)

		self.followingnumber = tk.Label(mainprofileframe,text = '0',bg = 'white',font = ('Ariel',30) )
		self.followingnumber.place(relx = 0.72,rely = 0.09)

		followinglabel=tk.Label(mainprofileframe, text="Following", bg='white', font=('bold'))
		followinglabel.place(relx=0.68,rely=0.16, relwidth=0.1, relheight=0.045)

		logout_button = tk.Button(mainprofileframe,text = "Logout",bg = "black",fg = "white",command = master.presslogoutbutton,font = ('bold',10))
		logout_button.place(relx = 0.89,rely = 0.03,relwidth = 0.1,relheight = 0.06)

		edit_button = tk.Button(mainprofileframe,text = 'Edit Profile', font=('bold'),bg = "black",fg = "white",command = master.presseditprofilebutton)
		edit_button.place(relx = 0.4, rely = 0.22, relwidth=0.38, relheight=0.037)

		mid_frame=tk.Frame(mainprofileframe,bg='white')
		mid_frame.place(relx=0.15, rely= 0.3, relheight=0.06, relwidth = 0.75)

		myposts_label=tk.Label(mid_frame,bg = "black",fg = "white", text=" My posts", font=('bold'))
		myposts_label.place(relx=0.1,rely=0.2, relwidth=0.8, relheight=0.85)

		imagepost_frame = tk.Frame(mainprofileframe, bg = 'white',relief='sunken')
		imagepost_frame.place(height=400,width=650, relx = 0.167, rely =0.38)


