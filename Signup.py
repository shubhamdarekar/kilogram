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
		mainsignup_frame.pack()

		signup_frame = tk.Frame(master.canvas,bg="#ebedd7")
		signup_frame.place(height = 500,width = 756,relx = 0.15,rely = 0.05)

		kilogramlabel2=tk.Label(signup_frame,text='Kilogram',font=35)
		kilogramlabel2.place(relx=0.2,rely=0.02,relwidth=0.6)

		firstnamelabel = tk.Label(signup_frame,bg = "#ebedd7",text = "First Name")
		firstnamelabel.place(relx = 0.3,rely = 0.1)

		self.firstnameentry = tk.Entry(signup_frame)
		self.firstnameentry.place(relx = 0.6,rely = 0.1)

		self.firstnameempty = tk.Label(signup_frame,text='', fg = 'red',bg="#ebedd7")
		self.firstnameempty.place(relx = 0.6, rely = 0.15)

		lastnamelabel = tk.Label(signup_frame,bg = "#ebedd7",text = "Last Name")
		lastnamelabel.place(relx = 0.3,rely = 0.2)

		self.lastnameentry = tk.Entry(signup_frame)
		self.lastnameentry.place(relx = 0.6,rely = 0.2)

		self.lastnameempty = tk.Label(signup_frame,text='', fg = 'red',bg="#ebedd7")
		self.lastnameempty.place(relx = 0.6, rely = 0.25)

		self.strvar = tk.StringVar(signup_frame)
		choices = range(13,100)

		agelabel = tk.Label(signup_frame,bg = "#ebedd7",text = "Age")
		agelabel.place(relx = 0.3,rely = 0.3)

		self.agechoice = tk.OptionMenu(signup_frame,self.strvar,choices[1],*choices)
		self.agechoice.place(relx = 0.6,rely = 0.3,relwidth = 0.17)
		self.strvar.set(18)
		# ageentry = tk.Entry(signup_frame)
		# ageentry.place(relx = 0.6,rely = 0.4)  

		emaillabel = tk.Label(signup_frame,bg = "#ebedd7",text = "Email ID")
		emaillabel.place(relx = 0.3,rely = 0.4)

		self.emailentry = tk.Entry(signup_frame)
		self.emailentry.place(relx = 0.6,rely = 0.4)

		self.emailempty = tk.Label(signup_frame,text='', fg = 'red',bg="#ebedd7")
		self.emailempty.place(relx = 0.6, rely = 0.45)

		phonenolabel = tk.Label(signup_frame,bg = "#ebedd7",text = "Phone Number")
		phonenolabel.place(relx = 0.3,rely = 0.5)

		self.phonenoentry = tk.Entry(signup_frame)
		self.phonenoentry.place(relx = 0.6,rely = 0.5)

		self.phonenoempty = tk.Label(signup_frame,text='', fg = 'red',bg="#ebedd7")
		self.phonenoempty.place(relx = 0.6, rely = 0.55)

		usernamelabel = tk.Label(signup_frame,bg = "#ebedd7",text = "Username")
		usernamelabel.place(relx = 0.3,rely = 0.6)

		self.usernameentry = tk.Entry(signup_frame)
		self.usernameentry.place(relx = 0.6,rely = 0.6)

		self.usernameempty = tk.Label(signup_frame,text='', fg = 'red',bg="#ebedd7")
		self.usernameempty.place(relx = 0.6, rely = 0.65)

		passwordlabel = tk.Label(signup_frame,bg = "#ebedd7",text = "Password")
		passwordlabel.place(relx = 0.3,rely = 0.7)

		self.passwordentry = tk.Entry(signup_frame,show = '*')
		self.passwordentry.place(relx = 0.6,rely = 0.7)

		self.passwordempty = tk.Label(signup_frame,text='', fg = 'red',bg="#ebedd7")
		self.passwordempty.place(relx = 0.6, rely = 0.75)

		confirmpasswordlabel = tk.Label(signup_frame,bg = "#ebedd7",text = "Confirm Password")
		confirmpasswordlabel.place(relx = 0.3,rely = 0.8)

		self.confirmpasswordentry = tk.Entry(signup_frame,show = '*')
		self.confirmpasswordentry.place(relx = 0.6,rely = 0.8)

		self.confirmpasswordempty = tk.Label(signup_frame,text='', fg = 'red',bg="#ebedd7")
		self.confirmpasswordempty.place(relx = 0.6, rely = 0.85)

		signup_button2= tk.Button(signup_frame,text = 'Signup',command = master.presssignup1)
		signup_button2.place(relx=0.4,rely=0.9,relwidth = 0.2)

		loginpage_frame = tk.Frame(master.canvas, bg = '#ebedd7',relief='raised')
		loginpage_frame.place(height=70,width=756, relx = 0.15, rely =0.8 )

		loginlabel = tk.Label(loginpage_frame,bg="#ebedd7", text = "Already a User?")
		loginlabel.pack()

		loginbutton = tk.Button(loginpage_frame,text="Login",command = master.presslogin)
		loginbutton.pack()


