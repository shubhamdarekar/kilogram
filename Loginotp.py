import tkinter as tk

class Loginotp(tk.Frame):
	def __init__(self,master):

		mainlogin_frame=tk.Frame(master.canvas,bg='white')
		mainlogin_frame.place(relheight=1, relwidth = 1)

		login_frame = tk.Frame(mainlogin_frame,bg="#ebedd7",relief='sunken')
		login_frame.place(height = 450,width = 756,relx = 0.15,rely = 0.1)

		kilogramlabel=tk.Label(login_frame,text='Kilogram',font=35)
		kilogramlabel.place(relx=0.2,rely=0.1,relwidth=0.6)

		# self.loginsuccesslabel = tk.Label(login_frame, text="", fg = 'green',bg="#ebedd7")
		# self.loginsuccesslabel.place(relx = 0.4, rely =0.2)

		otplabel = tk.Label(login_frame, text="OTP",bg="#ebedd7")
		otplabel.place(relx = 0.2, rely =0.3)

		self.otpentry = tk.Entry(login_frame)#,highlightcolor = 'blue')
		self.otpentry.place(relx = 0.4, rely = 0.3)
		self.otpentry.focus_set()

		self.otpempty = tk.Label(login_frame,text='', fg = 'red',bg="#ebedd7")
		self.otpempty.place(relx = 0.4,rely = 0.35)

		# passwordlabel = tk.Label(login_frame, text="Password",bg="#ebedd7")
		# passwordlabel.place(relx=0.2,rely=0.5)
		
		# self.passwordentry = tk.Entry(login_frame,show = '*')
		# self.passwordentry.place(relx=0.4,rely = 0.5)

		# self.passwordempty = tk.Label(login_frame,text='', fg = 'red',bg="#ebedd7")
		# self.passwordempty.place(relx = 0.4,rely = 0.55)

		otplogin_button = tk.Button(login_frame,text = 'Login',default = 'active',command = master.pressloginotp1)
		otplogin_button.place(relx = 0.4, rely = 0.7)

		signuppage_frame = tk.Frame(master.canvas, bg = '#ebedd7',relief='sunken')
		signuppage_frame.place(height=70,width=756, relx = 0.15, rely =0.8 )

		signup_label= tk.Label(signuppage_frame,text='New To kilogram? ')
		signup_label.pack()

		signup_button= tk.Button(signuppage_frame,text = 'Signup', command = master.presssignup)
		signup_button.pack()

	