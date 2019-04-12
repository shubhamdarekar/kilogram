<<<<<<< Updated upstream:kilogram/Login_page.py
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

		login_frame = tk.Frame(mainlogin_frame,bg="#ebedd7",relief='sunken')
		login_frame.place(height = 450,width = 756,relx = 0.15,rely = 0.1)

		kilogramlabel=tk.Label(login_frame,text='Kilogram',font=35)
		kilogramlabel.place(relx=0.2,rely=0.1,relwidth=0.6)

		self.loginsuccesslabel = tk.Label(login_frame, text="", fg = 'green',bg="#ebedd7")
		self.loginsuccesslabel.place(relx = 0.4, rely =0.2)

		usernamelabel = tk.Label(login_frame, text="Username",bg="#ebedd7")
		usernamelabel.place(relx = 0.2, rely =0.3)

		self.usernameentry = tk.Entry(login_frame)#,highlightcolor = 'blue')
		self.usernameentry.place(relx = 0.4, rely = 0.3)
		self.usernameentry.focus_set()

		self.usernameempty = tk.Label(login_frame,text='', fg = 'red',bg="#ebedd7")
		self.usernameempty.place(relx = 0.4,rely = 0.35)

		passwordlabel = tk.Label(login_frame, text="Password",bg="#ebedd7")
		passwordlabel.place(relx=0.2,rely=0.5)
		
		self.passwordentry = tk.Entry(login_frame,show = '*')
		self.passwordentry.place(relx=0.4,rely = 0.5)

		self.passwordempty = tk.Label(login_frame,text='', fg = 'red',bg="#ebedd7")
		self.passwordempty.place(relx = 0.4,rely = 0.55)

		login_button = tk.Button(login_frame,text = 'Login',default = 'active',command = master.presslogin1)
		login_button.place(relx = 0.4, rely = 0.7)

		signuppage_frame = tk.Frame(master.canvas, bg = '#ebedd7',relief='sunken')
		signuppage_frame.place(height=70,width=756, relx = 0.15, rely =0.8 )

		signup_label= tk.Label(signuppage_frame,text='New To kilogram? ',fg = 'green',bg = "#ebedd7")
		signup_label.pack()

		signup_button= tk.Button(signuppage_frame,text = 'Signup', command = master.presssignup)
		signup_button.pack()

=======
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

		login_frame = tk.Frame(mainlogin_frame,bg="#ebedd7",relief='sunken')
		login_frame.place(height = 450,width = 756,relx = 0.15,rely = 0.1)

		kilogramlabel=tk.Label(login_frame,text='Kilogram',font=35)
		kilogramlabel.place(relx=0.2,rely=0.1,relwidth=0.6)

		self.loginsuccesslabel = tk.Label(login_frame, text="", fg = 'green',bg="#ebedd7")
		self.loginsuccesslabel.place(relx = 0.4, rely =0.2)

		usernamelabel = tk.Label(login_frame, text="Username",bg="#ebedd7")
		usernamelabel.place(relx = 0.2, rely =0.3)

		self.usernameentry = tk.Entry(login_frame)#,highlightcolor = 'blue')
		self.usernameentry.place(relx = 0.4, rely = 0.3)
		self.usernameentry.focus_set()

		self.usernameempty = tk.Label(login_frame,text='', fg = 'red',bg="#ebedd7")
		self.usernameempty.place(relx = 0.4,rely = 0.35)

		passwordlabel = tk.Label(login_frame, text="Password",bg="#ebedd7")
		passwordlabel.place(relx=0.2,rely=0.5)
		
		self.passwordentry = tk.Entry(login_frame,show = '*')
		self.passwordentry.place(relx=0.4,rely = 0.5)

		self.passwordempty = tk.Label(login_frame,text='', fg = 'red',bg="#ebedd7")
		self.passwordempty.place(relx = 0.4,rely = 0.55)

		login_button = tk.Button(login_frame,text = 'Login',default = 'active',command = master.presslogin1)
		login_button.place(relx = 0.4, rely = 0.7)

		signuppage_frame = tk.Frame(master.canvas, bg = '#ebedd7',relief='sunken')
		signuppage_frame.place(height=70,width=756, relx = 0.15, rely =0.8 )

		signup_label= tk.Label(signuppage_frame,text='New To kilogram? ',fg = 'green',bg = "#ebedd7")
		signup_label.pack()

		signup_button= tk.Button(signuppage_frame,text = 'Signup', command = master.presssignup)
		signup_button.pack()

>>>>>>> Stashed changes:Login_page.py
