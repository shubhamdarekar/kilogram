import tkinter as tk
from skimage import io
import urllib
import cv2
from PIL import ImageTk, Image

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
		login_frame.place(height = 650,relwidth = 0.8,relx = 0.1,rely = 0)

		image = io.imread('https://firebasestorage.googleapis.com/v0/b/kilogramlikeinstagram.appspot.com/o/uiimages%2Fkilogram%20logo.png?alt=media&token=d11ac95f-6df1-4f2b-a198-620927a2a770')
		image = cv2.resize(image, (400,250), interpolation = cv2.INTER_AREA)
		image = Image.fromarray(image)
		image = ImageTk.PhotoImage(image)

		kilogramlabel=tk.Label(login_frame,image = image,bg ='white')
		kilogramlabel.place(relx=0.2,rely=0,relwidth=0.6)

		kilogramlabel.image = image


		self.loginsuccesslabel = tk.Label(login_frame, text="", fg = 'green',bg="white")
		self.loginsuccesslabel.place(relx = 0.35, rely =0.6,relwidth = 0.3)

		usernamelabel = tk.Label(login_frame, text="Username",bg="white",font=("Times", "20", "bold italic") )
		usernamelabel.place(relx = 0.3, rely =0.35)

		self.usernameentry = tk.Entry(login_frame)#,highlightcolor = 'blue')
		self.usernameentry.place(relx = 0.6, rely = 0.35)
		self.usernameentry.focus_set()

		self.usernameempty = tk.Label(login_frame,text='', fg = 'red',bg="white")
		self.usernameempty.place(relx = 0.4,rely = 0.4)

		passwordlabel = tk.Label(login_frame, text="Password",bg="white", font=("Times", "20", "bold italic"))
		passwordlabel.place(relx=0.3,rely=0.45)
		
		self.passwordentry = tk.Entry(login_frame,show = '*')
		self.passwordentry.place(relx=0.6,rely = 0.45)

		self.passwordempty = tk.Label(login_frame,text='', fg = 'red',bg="white")
		self.passwordempty.place(relx = 0.4,rely = 0.5)

		login_button = tk.Button(login_frame,text = 'Login',default = 'active',command = master.presslogin1, bg='black', fg='white')
		login_button.place(relx = 0.41, rely = 0.55, relwidth=0.2,relheight = 0.07)

		signuppage_frame = tk.Frame(master.canvas, bg = 'white',relief='sunken')
		signuppage_frame.place(relheight = 0.2,relwidth=0.8, relx = 0.1, rely =0.75)

		signup_label= tk.Label(signuppage_frame,text='New To kilogram? ',fg = 'black',bg = "white", font=("Motnotype Corsiva", "15", "bold italic"))
		signup_label.place(relx=0.40, rely=0.5,relwidth = 0.25)

		signup_button= tk.Button(signuppage_frame,text = 'Signup', command = master.presssignup, bg='black', fg='white')
		signup_button.place(relx=0.42, rely=0.69, relwidth=0.2,relheight = 0.3)


