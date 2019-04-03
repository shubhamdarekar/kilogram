import tkinter as tk 

class MyProfilePage(tk.Frame):
	def __init__(self,master):
		mainprofileframe = tk.Frame(master.navbar.midframe,bg = 'pink')
		mainprofileframe.place(relheight = '1',relwidth = 1)

		myprofilelabel=tk.Label(mainprofileframe, text="My Profile", bg='white', font=('bold'))
		myprofilelabel.place(relx=0.44,rely=0.07, relwidth=0.3, relheight=0.045)

		imagelabel=tk.Label(mainprofileframe)
		imagelabel.place(relx=0.22,rely=0.05,relwidth=0.15, relheight=0.18)

		username1label=tk.Label(mainprofileframe)
		username1label.place(relx=0.22,rely=0.25,relwidth=0.15, relheight=0.035)

		postslabel=tk.Label(mainprofileframe, text="Posts", bg='white', font=('bold'))
		postslabel.place(relx=0.4,rely=0.16, relwidth=0.1, relheight=0.045)

		followerslabel=tk.Label(mainprofileframe, text="Followers", bg='white', font=('bold'))
		followerslabel.place(relx=0.54,rely=0.16, relwidth=0.1, relheight=0.045)

		followinglabel=tk.Label(mainprofileframe, text="Following", bg='white', font=('bold'))
		followinglabel.place(relx=0.68,rely=0.16, relwidth=0.1, relheight=0.045)

		edit_button = tk.Button(mainprofileframe,text = 'Edit Profile', font=('bold'))
		edit_button.place(relx = 0.4, rely = 0.22, relwidth=0.38, relheight=0.037)

		mid_frame=tk.Frame(mainprofileframe,bg='white')
		mid_frame.place(relx=0.15, rely= 0.3, relheight=0.06, relwidth = 0.75)

		myposts_button=tk.Button(mid_frame, text=" My posts", font=('bold'))
		myposts_button.place(relx=0.09,rely=0.09, relwidth=0.278, relheight=0.85)

		grid_button=tk.Button(mid_frame, text="Grid", font=('bold'))
		grid_button.place(relx=0.37,rely=0.09, relwidth=0.278, relheight=0.85)

		tags_button=tk.Button(mid_frame, text="Tag", font=('bold'))
		tags_button.place(relx=0.65,rely=0.09, relwidth=0.278, relheight=0.85)

		imagepost_frame = tk.Frame(mainprofileframe, bg = '#ebedd7',relief='sunken')
		imagepost_frame.place(height=400,width=650, relx = 0.167, rely =0.38)
