import tkinter as tk

class Signup_page(tk.Frame):
	def __init__(self,master):
		# global signup_frame
		# global firstnamelabel
		# global firstnameentry
		# global lastnamelabel
		# global lastnameentry
		# global phonenolabel
		# global phonenoentry
		# global emaillabel
		# global emailentry
		# global passwordlabel
		# global passwordentry
		# global confirmpasswordlabel
		# global confirmpasswordentry
		# global usernamelabel
		# global usernameentry
		# global agelabel
		# global ageentry
		# global strvar
		# global agechoice
		# global kilogramlabel2
		# global loginpage_frame
		# global loginlabel
		# global loginbutton
		# global mainlogin_frame

		mainsignup_frame=tk.Frame(master.canvas,bg='white')
		mainsignup_frame.place(relx = 1,rely = 1)

		signup_frame = tk.Frame(master.canvas,bg="white")
		signup_frame.place(height = 500,width = 756,relx = 0.15,rely = 0.05)

		kilogramlabel2=tk.Label(signup_frame,text='Kilogram',font=("Motnotype Corsiva", "25", "bold italic"), bg='white')
		kilogramlabel2.place(relx=0.3,rely=0.0009,relwidth=0.6)

		firstnamelabel = tk.Label(signup_frame,bg = "white",text = "First Name",font=("Times", "18", "bold italic"))
		firstnamelabel.place(relx = 0.3,rely = 0.1)

		self.firstnameentry = tk.Entry(signup_frame)
		self.firstnameentry.place(relx = 0.6,rely = 0.1)

		self.firstnameempty = tk.Label(signup_frame,text='', fg = 'red',bg="white")
		self.firstnameempty.place(relx = 0.6, rely = 0.15)

		lastnamelabel = tk.Label(signup_frame,bg = "white",text = "Last Name",font=("Times", "18", "bold italic"))
		lastnamelabel.place(relx = 0.3,rely = 0.2)

		self.lastnameentry = tk.Entry(signup_frame)
		self.lastnameentry.place(relx = 0.6,rely = 0.2)

		self.lastnameempty = tk.Label(signup_frame,text='', fg = 'red',bg="white")
		self.lastnameempty.place(relx = 0.6, rely = 0.25)

		self.strvar = tk.StringVar(signup_frame)
		choices = range(13,100)

		agelabel = tk.Label(signup_frame,bg = "white",text = "Age",font=("Times", "18", "bold italic"))
		agelabel.place(relx = 0.3,rely = 0.3)

		self.agechoice = tk.OptionMenu(signup_frame,self.strvar,choices[1],*choices)
		self.agechoice.place(relx = 0.6,rely = 0.3,relwidth = 0.17)
		self.strvar.set(18)
		# ageentry = tk.Entry(signup_frame)
		# ageentry.place(relx = 0.6,rely = 0.4)  

		emaillabel = tk.Label(signup_frame,bg = "white",text = "Email ID",font=("Times", "18", "bold italic"))
		emaillabel.place(relx = 0.3,rely = 0.4)

		self.emailentry = tk.Entry(signup_frame)
		self.emailentry.place(relx = 0.6,rely = 0.4)

		self.emailempty = tk.Label(signup_frame,text='', fg = 'red',bg="white")
		self.emailempty.place(relx = 0.6, rely = 0.45)

		phonenolabel = tk.Label(signup_frame,bg = "white",text = "Phone Number",font=("Times", "18", "bold italic"))
		phonenolabel.place(relx = 0.3,rely = 0.5)

		self.phonenoentry = tk.Entry(signup_frame)
		self.phonenoentry.place(relx = 0.6,rely = 0.5)

		self.phonenoempty = tk.Label(signup_frame,text='', fg = 'red',bg="white")
		self.phonenoempty.place(relx = 0.6, rely = 0.55)

		usernamelabel = tk.Label(signup_frame,bg = "white",text = "Username",font=("Times", "18", "bold italic"))
		usernamelabel.place(relx = 0.3,rely = 0.6)

		self.usernameentry = tk.Entry(signup_frame)
		self.usernameentry.place(relx = 0.6,rely = 0.6)

		self.usernameempty = tk.Label(signup_frame,text='', fg = 'red',bg="white")
		self.usernameempty.place(relx = 0.6, rely = 0.65)

		passwordlabel = tk.Label(signup_frame,bg = "white",text = "Password",font=("Times", "18", "bold italic"))
		passwordlabel.place(relx = 0.3,rely = 0.7)

		self.passwordentry = tk.Entry(signup_frame,show = '*')
		self.passwordentry.place(relx = 0.6,rely = 0.7)

		self.passwordempty = tk.Label(signup_frame,text='', fg = 'red',bg="white")
		self.passwordempty.place(relx = 0.6, rely = 0.75)

		confirmpasswordlabel = tk.Label(signup_frame,bg = "white",text = "Confirm Password",font=("Times", "18", "bold italic"))
		confirmpasswordlabel.place(relx = 0.3,rely = 0.8)

		self.confirmpasswordentry = tk.Entry(signup_frame,show = '*')
		self.confirmpasswordentry.place(relx = 0.6,rely = 0.8)

		self.confirmpasswordempty = tk.Label(signup_frame,text='', fg = 'red',bg="white")
		self.confirmpasswordempty.place(relx = 0.6, rely = 0.85)

		signup_button2= tk.Button(signup_frame,text = 'Send OTP to Mobile Number',command = master.presssignup1, bg='black', fg='white')
		signup_button2.place(relx=0.3,rely=0.9,relwidth = 0.25)

		signup_button3= tk.Button(signup_frame,text = 'Send Otp To Email Id',command = master.presssignup2, bg='black', fg='white')
		signup_button3.place(relx=0.6,rely=0.9,relwidth = 0.25)

		loginpage_frame = tk.Frame(master.canvas, bg = 'white',relief='raised')
		loginpage_frame.place(relheight=0.1,relwidth=0.7, relx = 0.15, rely =0.76 )

		loginlabel = tk.Label(loginpage_frame,bg="white", text = "Already a User?",fg = 'green',font=("Times", "18", "bold italic"))
		loginlabel.pack()

		loginbutton = tk.Button(loginpage_frame,text="Login",command = master.presslogin,bg='black',fg='white')
		loginbutton.pack()


