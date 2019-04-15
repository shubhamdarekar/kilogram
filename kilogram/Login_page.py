import tkinter as tk


class Login_page(tk.Frame):
	def __init__(self,master):
		# global usernamelabel
		# global usernameentry
		# global passwordlabel
		# global passwordentry
		# global login_frame
		# global signuppage_frame
		# global kilogramlabel
		# global login_button
		# global signup_label
		# global signup_button
		# global mainlogin_frame

		

		mainlogin_frame=tk.Frame(master.canvas,bg='white')
		mainlogin_frame.place(relheight=1, relwidth = 1)

		login_frame = tk.Frame(mainlogin_frame,bg="white",relief='sunken')
		login_frame.place(height = 450,width = 756,relx = 0.15,rely = 0.1)

		kilogramlabel=tk.Label(login_frame,text='Kilogram',font=("Motnotype Corsiva", "50", "bold italic"), bg='white')
		kilogramlabel.place(relx=0.2,rely=0.01,relwidth=0.6)

		self.loginsuccesslabel = tk.Label(login_frame, text="", fg = 'green',bg="white")
		self.loginsuccesslabel.place(relx = 0.4, rely =0.2)

		usernamelabel = tk.Label(login_frame, text="Username",bg="white",font=("Times", "25", "bold italic") )
		usernamelabel.place(relx = 0.2, rely =0.3)

		self.usernameentry = tk.Entry(login_frame)#,highlightcolor = 'blue')
		self.usernameentry.place(relx = 0.5, rely = 0.34)
		self.usernameentry.focus_set()

		self.usernameempty = tk.Label(login_frame,text='', fg = 'red',bg="white")
		self.usernameempty.place(relx = 0.4,rely = 0.4)

		passwordlabel = tk.Label(login_frame, text="Password",bg="white", font=("Times", "25", "bold italic"))
		passwordlabel.place(relx=0.2,rely=0.5)
		
		self.passwordentry = tk.Entry(login_frame,show = '*')
		self.passwordentry.place(relx=0.5,rely = 0.53)

		self.passwordempty = tk.Label(login_frame,text='', fg = 'red',bg="white")
		self.passwordempty.place(relx = 0.4,rely = 0.59)

		login_button = tk.Button(login_frame,text = 'Login',default = 'active',command = master.presslogin1, bg='black', fg='white')
		login_button.place(relx = 0.41, rely = 0.7, relwidth=0.15,)

		signuppage_frame = tk.Frame(master.canvas, bg = 'white',relief='sunken')
		signuppage_frame.place(height=70,width=756, relx = 0.15, rely =0.7)

		signup_label= tk.Label(signuppage_frame,text='New To kilogram? ',fg = 'black',bg = "white", font=("Motnotype Corsiva", "25", "bold italic"))
		signup_label.pack()

		signup_button= tk.Button(signuppage_frame,text = 'Signup', command = master.presssignup, bg='black', fg='white')
		signup_button.place(relx=0.41, rely=0.69, relwidth=0.17)

