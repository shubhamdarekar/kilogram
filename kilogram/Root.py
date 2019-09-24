# import AppKit
import tkinter as tk
from tkinter import ttk
import Login_page
import Signup
# import urllib.request
# import urllib.parse
import pyrebase
import smtplib
import LowerNavbar
import pymysql
import re
import urllib.request
import urllib.parse
import math
import random
import Loginotp
import HomePage
import SearchPage
import AddPostPage
import NotificationsPage
import MyProfilePage
import requests
import EditProfile
import ChangeUsername
import ChangePassword
import DM_Page
from tkinter import filedialog
from PIL import ImageTk, Image
import AddCaptionPage
import Chat
import EnterPassword
import numpy as np
import urllib
import urllib.error
from skimage import io
import cv2
import tkinter.font
#import ChangeProfilePicture
import CameraPage


class Root(tk.Frame):
	def __init__(self,master):
		tk.Frame.__init__(self,master)
		self.master.resizable(False,False)
		self.master.geometry('+100+20')
		self.master.protocol('WM_DELETE_WINDOW',self.clickcancel)
		self.master.bind('<Escape>',self.clickEscape)
		self.master.title('Kilogram')
		#self.master.config(menu= tk.Menu(self.master))
		self.pack()
		self.canvas = tk.Canvas(root,height=700,width=1080,bg="white").pack()
		self.loginpage = Login_page.Login_page(self)
		
		#abc = test.PickFiles(self.canvas)
	def connecttodatabase(self):
		self.mydb = pymysql.connect(host="localhost",user="root",passwd="",db="kilogram")
		self.mc = self.mydb.cursor()
		return self.mc

	# def insertinUser(self, cursor,fname,lname,age,phnno,emailid,username ):
	# 	cursor.execute('INSERT into user (fname,lname,age,phoneNo,emailid,username) values ("%s","%s","%s","%s","%s,"%s")'%(fname,lname,age,phnno,emailid,username))
	# 	cursor.commit()

	def sendSMS(self,apikey, numbers, sender, message):
		data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
			'message' : message, 'sender': sender})
		data = data.encode('utf-8')
		try : 
			request = urllib.request.Request("https://api.txtlocal.com/send/?")
			f = urllib.request.urlopen(request, data)
			fr = f.read()
		except urllib.error.URLError :

			print("Error")
		else:
			return(fr)
	#https://maker.ifttt.com/trigger/{event}/with/key/iPUGsUMmzf9dS90kfOlajV45ZiaYPlDKV-bFvelUqh9
	def presscamerabutton(self):
		self.camerapage = CameraPage.CameraPage(self)
		if self.camerapage.flag == 1:
			self.filepath = 'user.png'
			self.addpostpage = AddPostPage.AddPostPage(self)
			try:
				img =tk.PhotoImage(file = self.filepath)
				# if im.shape[0]>300:
				# 	image = cv2.resize(image, (600,300), interpolation = cv2.INTER_AREA)
				# self.newlabel = tk.Canvas(self.addpostpage.filelabel,width = 1000,height = 1000,bg='red')
				# self.newlabel.pack()
			except (tk.TclError):
				self.addpostpage.filelabel.configure(text = 'Please Upload a image png File.',fg = 'red')
			else:
				self.addpostpage.filelabel.configure(image = img)
			self.mainloop()
		else:
			self.presshomebutton()

	def sendemail(self,emailid, otp):
	    # report = {}
	    # report["value1"] = emailid
	    # report["value2"] = otp
	    # return requests.post("https://maker.ifttt.com/trigger/OtpKilogram/with/key/iPUGsUMmzf9dS90kfOlajV45ZiaYPlDKV-bFvelUqh9",data = report)
	    s = smtplib.SMTP('smtp.gmail.com', 587)
	    s.starttls()
	    s.login("kilogramapplikeinstagram@gmail.com", "qwerty@1234")
	    message = "Great Choice choosing Kilogram. In order to login into your account,your One Time Password is %s"%(otp)
	    s.sendmail("kilogramapplikeinstagram@gmail.com",emailid, message)
	    s.quit()



	
	def clickcancel(self):
		self.abc = tk.Toplevel()
		self.abc.geometry('+600+330')
		l = tk.Label(self.abc,text = 'Do You Want to Close it?')
		l.grid(row = 0,column= 2)
		b1 = tk.Button(self.abc,text = 'Exit',command = self.exit)
		b1.grid(row = 3,column= 3)
		b2 = tk.Button(self.abc,text = 'Cancel',command = self.cancel)
		b2.grid(row = 3,column= 1)
		self.abc.title('Exit')
	def exit(self):
		self.abc.destroy()
		self.master.destroy()
	def cancel(self):
		self.abc.destroy()

	def clickEscape(self,event):
		self.abc = tk.Toplevel()
		l = tk.Label(self.abc,text = 'Do You Want to Close it?')
		l.pack()
		b1 = tk.Button(self.abc,text = 'Exit',command = self.exit)
		b1.grid(row = 0,column= 1)
		b2 = tk.Button(self.abc,text = 'Cancel',command = self.cancel)
		b2.grid(row = 0,column= 0)
		

	def _toggle_state(self,widget,state):
		state = state if state in ('normal','disabled') else 'normal'
		widget.configure(state = state)

	def presssignup(self):
		self.signuppage = Signup.Signup_page(self)

	def generateOTP(self) : 
		digits = "0123456789"
		OTP = "" 
		for i in range(6) : 
			OTP += digits[math.floor(random.random() * 10)] 
  
		return OTP

	def presssignup1(self):
		fname = self.signuppage.firstnameentry.get()
		lname = self.signuppage.lastnameentry.get()
		age = self.signuppage.strvar.get()
		email = self.signuppage.emailentry.get()
		phnno = self.signuppage.phonenoentry.get()
		username = self.signuppage.usernameentry.get()
		password = self.signuppage.passwordentry.get()
		cnfpassword = self.signuppage.confirmpasswordentry.get()
		#print(fname,lname,age,email,phnno,password)
		self.signuppage.firstnameempty.configure(text = '')
		self.signuppage.lastnameempty.configure(text = '')
		self.signuppage.emailempty.configure(text = '')
		self.signuppage.phonenoempty.configure(text = '')
		self.signuppage.usernameempty.configure(text = '')
		self.signuppage.passwordempty.configure(text = '')
		self.signuppage.confirmpasswordempty.configure(text = '')		
		flag = 1
		if fname == '':
			self.signuppage.firstnameempty.configure(text = 'First name Cannot be Empty!!!')
			flag = 0
		if lname == '':
			self.signuppage.lastnameempty.configure(text = 'Last name Cannot be Empty!!!')
			flag = 0
		if email == '':
			self.signuppage.emailempty.configure(text = 'Email Address Cannot be Empty!!!')
			flag = 0
		if phnno == '':
			self.signuppage.phonenoempty.configure(text = 'Phone number Cannot be Empty!!!')
			flag = 0
		if username == '':
			self.signuppage.usernameempty.configure(text = 'Username number Cannot be Empty!!!')
			flag = 0
		if password == '':
			self.signuppage.passwordempty.configure(text = 'Password Cannot be Empty!!!')
			flag = 0
		if cnfpassword == '':
			self.signuppage.confirmpasswordempty.configure(text = 'This field Cannot be Empty!!!')
			flag = 0
		if len(fname) >= 25:
			self.signuppage.firstnameempty.configure(text = 'Length of First name should not be more than 25!!!')
			flag = 0
		if len(lname) >= 25:
			self.signuppage.lastnameempty.configure(text = 'Length of Last name should not be more than 25!!!')
			flag = 0
		if len(username) >=20:
			self.signuppage.usernameempty.configure(text = 'Length of Username should not be more than 20!!!')
			flag = 0
		if len(phnno) >10:
			self.signuppage.phonenoempty.configure(text = 'Length of Phone number should not be more than 10!!!')
			flag = 0
		if not phnno.isdigit():
			self.signuppage.phonenoempty.configure(text = 'Phone number should have only numbers.')
			flag = 0
		if not username.isalnum():
			self.signuppage.usernameempty.configure(text = 'Username should contain only numbers and digits.!!!')
			flag = 0
		if not fname.isalnum():
			self.signuppage.firstnameempty.configure(text = 'First name should have only letters!!!')
			flag = 0
		if not lname.isalnum():
			self.signuppage.lastnameempty.configure(text = 'Last name should have only letters!!!')
			flag = 0

		if flag == 1:
			self.signuppage.firstnameempty.configure(text = '')
			self.signuppage.lastnameempty.configure(text = '')
			self.signuppage.emailempty.configure(text = '')
			self.signuppage.phonenoempty.configure(text = '')
			self.signuppage.passwordempty.configure(text = '')
			self.signuppage.confirmpasswordempty.configure(text = '')
			if cnfpassword != password :
				self.signuppage.confirmpasswordempty.configure(text = "Passord doesn't match")
			else :
				flag = 0
				self.mc = self.connecttodatabase()
				self.mc.execute("select username from user")
				self.usernameli = self.mc.fetchall()
				self.usernameli = list(sum(self.usernameli, ()))
				if username in self.usernameli:
					self.signuppage.usernameempty.configure(text = 'Username already exists!! Try another username')
					flag = 1
				self.mc.execute("select phoneNo from user")
				self.phnnoli = self.mc.fetchall()
				# print(self.phnnoli)
				self.phnnoli = list(sum(self.phnnoli, ()))
				# print((self.phnnoli))
				if (phnno) in self.phnnoli :
					self.signuppage.phonenoempty.configure(text = 'Phone Number already exists!! Use another phone number!!')
					flag = 1
				self.mc.execute("select emailid from user")
				self.emailidli = self.mc.fetchall()
				self.emailidli = list(sum(self.emailidli, ()))
				if email in self.emailidli :
					self.signuppage.emailempty.configure(text = 'Email Id already exists!! Use another Email Id')
					flag = 1
				if flag == 0:
					self.otp = self.generateOTP()
					print(self.otp)
					self.loginotp = Loginotp.Loginotp(self)
					self.resp =  self.sendSMS('/apikey/', '+91%s'%(phnno),'Kilogram', 'Great Choice choosing Kilogram. In order to login into your account,your One Time Password is %s'%(str(self.otp)))
					print(self.resp)
					self.loginotp = Loginotp.Loginotp(self)
					
	def presssignup2(self):
		self.signuppage.firstnameempty.configure(text = '')
		self.signuppage.lastnameempty.configure(text = '')
		self.signuppage.emailempty.configure(text = '')
		self.signuppage.phonenoempty.configure(text = '')
		self.signuppage.usernameempty.configure(text = '')
		self.signuppage.passwordempty.configure(text = '')
		self.signuppage.confirmpasswordempty.configure(text = '')
		fname = self.signuppage.firstnameentry.get()
		lname = self.signuppage.lastnameentry.get()
		age = self.signuppage.strvar.get()
		email = self.signuppage.emailentry.get()
		phnno = self.signuppage.phonenoentry.get()
		username = self.signuppage.usernameentry.get()
		password = self.signuppage.passwordentry.get()
		cnfpassword = self.signuppage.confirmpasswordentry.get()
		#print(fname,lname,age,email,phnno,password)
		flag = 1
		if fname == '':
			self.signuppage.firstnameempty.configure(text = 'First name Cannot be Empty!!!')
			flag = 0
		if lname == '':
			self.signuppage.lastnameempty.configure(text = 'Last name Cannot be Empty!!!')
			flag = 0
		if email == '':
			self.signuppage.emailempty.configure(text = 'Email Address Cannot be Empty!!!')
			flag = 0
		if phnno == '':
			self.signuppage.phonenoempty.configure(text = 'Phone number Cannot be Empty!!!')
			flag = 0
		if username == '':
			self.signuppage.usernameempty.configure(text = 'Username number Cannot be Empty!!!')
			flag = 0
		if password == '':
			self.signuppage.passwordempty.configure(text = 'Password Cannot be Empty!!!')
			flag = 0
		if cnfpassword == '':
			self.signuppage.confirmpasswordempty.configure(text = 'This field Cannot be Empty!!!')
			flag = 0
		if len(fname) >= 25:
			self.signuppage.firstnameempty.configure(text = 'Length of First name should not be more than 25!!!')
			flag = 0
		if len(lname) >= 25:
			self.signuppage.lastnameempty.configure(text = 'Length of Last name should not be more than 25!!!')
			flag = 0
		if len(username) >=20:
			self.signuppage.usernameempty.configure(text = 'Length of Username should not be more than 20!!!')
			flag = 0
		if len(phnno) >10:
			self.signuppage.phonenoempty.configure(text = 'Length of Phone number should not be more than 10!!!')
			flag = 0
		if not phnno.isdigit():
			self.signuppage.phonenoempty.configure(text = 'Phone number should have only numbers.')
			flag = 0
		if not username.isalnum():
			self.signuppage.usernameempty.configure(text = 'Username should contain only numbers and digits.!!!')
			flag = 0
		if not fname.isalnum():
			self.signuppage.firstnameempty.configure(text = 'First name should have only letters!!!')
			flag = 0
		if not lname.isalnum():
			self.signuppage.lastnameempty.configure(text = 'Last name should have only letters!!!')
			flag = 0

		if flag == 1:
			self.signuppage.firstnameempty.configure(text = '')
			self.signuppage.lastnameempty.configure(text = '')
			self.signuppage.emailempty.configure(text = '')
			self.signuppage.phonenoempty.configure(text = '')
			self.signuppage.passwordempty.configure(text = '')
			self.signuppage.confirmpasswordempty.configure(text = '')
			if cnfpassword != password :
				self.signuppage.confirmpasswordempty.configure(text = "Passord doesn't match")
			else :
				flag = 0
				self.mc = self.connecttodatabase()
				self.mc.execute("select username from user")
				self.usernameli = self.mc.fetchall()
				self.usernameli = list(sum(self.usernameli, ()))
				if username in self.usernameli:
					self.signuppage.usernameempty.configure(text = 'Username already exists!! Try another username')
					flag = 1
				self.mc.execute("select phoneNo from user")
				self.phnnoli = self.mc.fetchall()
				# print(self.phnnoli)
				self.phnnoli = list(sum(self.phnnoli, ()))
				# print((self.phnnoli))
				if (phnno) in self.phnnoli :
					self.signuppage.phonenoempty.configure(text = 'Phone Number already exists!! Use another phone number!!')
					flag = 1
				self.mc.execute("select emailid from user")
				self.emailidli = self.mc.fetchall()
				self.emailidli = list(sum(self.emailidli, ()))
				if email in self.emailidli :
					self.signuppage.emailempty.configure(text = 'Email Id already exists!! Use another Email Id')
					flag = 1
				if flag == 0:
					self.otp = self.generateOTP()
					print(self.otp)
					self.loginotp = Loginotp.Loginotp(self)
					self.emailotp = self.sendemail(email,self.otp)
					print(self.emailotp)
					

	def pressloginotp1(self):
		fname = self.signuppage.firstnameentry.get()
		lname = self.signuppage.lastnameentry.get()
		age = self.signuppage.strvar.get()
		email = self.signuppage.emailentry.get()
		phnno = self.signuppage.phonenoentry.get()
		username = self.signuppage.usernameentry.get()
		password = self.signuppage.passwordentry.get()
		cnfpassword = self.signuppage.confirmpasswordentry.get()
		if self.loginotp.otpentry.get() == '':
			self.loginotp.otpempty.configure(text='Otp box cannot be empty.')
		else :
			if self.loginotp.otpentry.get() == self.otp:
				self.mc.execute('INSERT into user (fname,lname,age,phoneNo,emailid,username) values ("%s","%s",%s,"%s","%s","%s")'%(fname,lname,age,phnno,email,username))
				self.mydb.commit()
				self.mc.execute('SELECT uid from user where username = "%s"'%(username))
				self.uidli = self.mc.fetchall()
				self.uidli = list(sum(self.uidli,()))
				self.mc.execute('INSERT into auth (uid,passwd) values (%s,"%s")'%(self.uidli[0],password))
				self.mydb.commit()
				self.loginpage = Login_page.Login_page(self)
				self.loginpage.loginsuccesslabel.configure(text = 'Signup successfull!!!')
			else :
				self.loginotp.otpempty.configure(text = "Invalid otp")

	def presslogin(self):
		self.loginpage = Login_page.Login_page(self)


	def presslogin1(self):
		self.loginpage.usernameempty.configure(text = '')
		self.loginpage.passwordempty.configure(text = '')
		username = self.loginpage.usernameentry.get()
		password = self.loginpage.passwordentry.get()

		if username =='' or password == '':
			if username == '':
				self.loginpage.usernameempty.configure(text = 'Username Cannot be empty!!!')
			if password == '':
				self.loginpage.passwordempty.configure(text = 'Password Cannot be empty!!!')
		else:
			self.loginpage.usernameempty.configure(text = '')
			self.loginpage.passwordempty.configure(text = '')
			self.mc = self.connecttodatabase()
			self.mc.execute("select username from user")
			self.usernameli = self.mc.fetchall()
			self.usernameli = list(sum(self.usernameli, ()))
			if username not in self.usernameli :
				self.loginpage.usernameempty.configure(text = 'The Username entered was wrong.')
				self.loginpage.usernameentry.delete(0,100)
				self.loginpage.passwordentry.delete(0,100)
			else:
				self.username = username
				self.sql = 'SELECT uid from user where username ="%s" '
				self.mc.execute(self.sql % username)
				self.uidli = self.mc.fetchall()
				self.uidli = list(sum(self.uidli, ()))
				self.uid = self.uidli[0]
				self.sql2 = 'select passwd from auth where uid = "%s" '
				self.mc.execute(self.sql2,self.uid)
				self.passwordli = self.mc.fetchall()
				self.passwordli = list(sum(self.passwordli, ()))
				if password in self.passwordli:
					# self.navbar = LowerNavbar.Lowernavbar(self)
					# self.homepage = HomePage.HomePage(self)
					self.presshomebutton()
				else :
					self.loginpage.passwordempty.configure(text = 'Password is incorrect!!!')
					self.loginpage.passwordentry.delete(0,100)


	def presshomebutton(self):
		self.navbar = LowerNavbar.Lowernavbar(self)
		self.homepage = HomePage.HomePage(self)

		sql = 'SELECT fuid from friends where uid = "%s"'
		args =self.uid
		self.mc = self.connecttodatabase()
		self.mc.execute(sql,args)
		friends = self.mc.fetchall()
		friends = list(sum(friends, ()))
		print(friends)

		pids = []
		for f in friends:
			sql = 'SELECT pid from posts where uid = %s'
			self.mc.execute(sql,f)
			p = self.mc.fetchall()
			p = list(sum(p, ()))
			pids= pids+p

		pids = sorted(pids,reverse=True)
		print(pids)

		uuu = []
		imm = []
		cpp = []
		for p in pids:
			sql = 'SELECT username from user where uid =(SELECT uid from posts where pid = %s)'
			self.mc.execute(sql%p)
			g = self.mc.fetchall()
			g = list(sum(g, ()))
			uuu+=g

			sql = 'SELECT imgs from posts where pid = %s'
			self.mc.execute(sql,p)
			im = self.mc.fetchall()
			im = list(sum(im, ()))
			imm+=im

			sql = 'SELECT caption from posts where pid = %s'
			self.mc.execute(sql,p)
			cp = self.mc.fetchall()
			cp = list(sum(cp, ()))
			cpp+=cp

		self.abc = list(map(list,zip(uuu,pids,imm,cpp)))
		#print(abc)

		self.index1 = 0

		if len(self.abc)>0:
			self.nextpost1()
		else:
			self._toggle_state(self.homepage.nextbutton,'disabled')
			self._toggle_state(self.homepage.prevbutton,'disabled')
			self.homepage.postlabel.configure(text = 'No Posts Try to follow few people.')

	def nextbutton1(self):
		self._toggle_state(self.homepage.prevbutton,'enabled')
		self.index1+=1
		self.nextpost1()
		

	def prevbutton1(self):
		self._toggle_state(self.homepage.nextbutton,'enabled')
		self.index1-=1
		self.prevpost1()
		

	def nextpost1(self):
		if(self.index1<=len(self.abc)-1 and self.index1>=0):
			image = io.imread(self.abc[self.index1][2])
			if image.shape[0]>300:
				image = cv2.resize(image, (600,300), interpolation = cv2.INTER_AREA)
			image = Image.fromarray(image)
			image = ImageTk.PhotoImage(image)
			self.homepage.usernamelabel.configure(text = self.abc[self.index1][0])
			self.homepage.captionlabel.configure(text = self.abc[self.index1][0])
			self.homepage.captionmsg.configure(text = self.abc[self.index1][3])
			self.homepage.postlabel.configure(image = image)
			self.mainloop()
		elif self.index1<0:
			self._toggle_state(self.homepage.nextbutton,'disabled')
			self.homepage.postlabel.configure(image = '',text = 'Press Next once more',fg = 'red')
		else:
			self._toggle_state(self.homepage.nextbutton,'disabled')
			self.homepage.usernamelabel.configure(text = "")
			self.homepage.captionlabel.configure(text = "")
			self.homepage.captionmsg.configure(text = "")
			self.homepage.postlabel.configure(image = '',text = 'No More Images,Press Previous',fg = 'red')

	def prevpost1(self):
		if(self.index1>=0 and self.index1<=len(self.abc)-1):
			image = io.imread(self.abc[self.index1][2])
			if image.shape[0]>300:
				image = cv2.resize(image, (600,300), interpolation = cv2.INTER_AREA)
			image = Image.fromarray(image)
			image = ImageTk.PhotoImage(image)
			self.homepage.usernamelabel.configure(text = self.abc[self.index1][0])
			self.homepage.captionlabel.configure(text = self.abc[self.index1][0])
			self.homepage.captionmsg.configure(text = self.abc[self.index1][3])
			self.homepage.postlabel.configure(image = image)
			self.mainloop()
		elif self.index1>len(self.abc)-1:
			self._toggle_state(self.homepage.prevbutton,'disabled')
			self.homepage.postlabel.configure(image = '',text = 'Press Previous once more',fg = 'red')
		else:
			self._toggle_state(self.homepage.prevbutton,'disabled')
			self.homepage.usernamelabel.configure(text = "")
			self.homepage.captionlabel.configure(text = "")
			self.homepage.captionmsg.configure(text = "")
			self.homepage.postlabel.configure(image = '',text = 'No More Images,Press Next',fg = 'red')
			


	def presssearchbutton(self):
		self.searchpage = SearchPage.SearchPage(self)

	def presssearchbutton1(self):
		# self.fusername = self.searchpage.search_entry.get()
		# self.searchpage = SearchPage.SearchPage(self)
		# sql = 'SELECT username from user where username like "%s"'
		# self.mc.execute(sql % ("%"+self.fusername+"%"))
		# self.unames = self.mc.fetchall()


		# if self.unames == 0:
		# 	label = tk.Label(self.searchpage.frame,text = "No users found",bg = "white",fg = "black",font = ('bold',20))
		# 	label.place(relwidth = 1,reheight = 0.1, rely = 0.4)
		# else:
		# 	self.unames = list(sum(self.unames, ())) 
		# 	entry = {}
		# 	label = {}

		# 	i = 0
		# 	for name in self.unames:
		# 		e = tk.Button(self.searchpage.frame,text = 'Follow')
		# 		e.grid(sticky='w')
		# 		entry[name] = e

		# 		lb = tk.Label(self.searchpage.frame, text=name, bg = 'white')
		# 		lb.grid(row=i, column=1)
		# 		label[name] = lb
		# 		i += 1

		self.fusername = self.searchpage.search_entry.get()
		self.searchpage = SearchPage.SearchPage(self)
		sql = 'SELECT username from user where username = "%s"'
		self.mc.execute(sql % self.fusername)
		self.unames = self.mc.fetchall()
		self.unames = list(sum(self.unames, ()))
		entry = {}
		i = 0
		j = 0.05
		helv36 = tk.font.Font(family='Helvetica', size=30, weight='bold')
		for name in self.unames:
			self.e = tk.Button(self.searchpage.frame,font = helv36,text = "Follow "+self.unames[i],bg = "black",fg = "white",command = self.pressfollowbutton)
			self.e.place(relheight = 0.1,relwidth = 1,rely = j)
			entry[name] =self.e
			j += 0.12
			i += 1

		sql = 'SELECT fuid from friends where uid = (SELECT uid from user where username = "%s")'
		self.mc.execute(sql % self.username)
		followers = self.mc.fetchall()
		followers = list(sum(followers, ()))
		print(followers)
		sql = 'SELECT uid from user where username = "%s"'
		self.mc.execute(sql % self.fusername)
		self.d = self.mc.fetchall()
		self.d = list(sum(self.d, ()))
		if(len(self.d) == 0):
			self.e1 = tk.Button(self.searchpage.frame,font = helv36,text = "No Users Found",bg = "black",fg = "white",command = self.pressfollowbutton)
			self.e1.place(relheight = 0.1,relwidth = 1,rely = 0.17)
			# self.e1.configure(text = "No Users Found ")
		else:
			print(self.d[0])
			print(self.uid)
			if(self.d[0] == self.uid):
				self._toggle_state(self.e,'disabled')
				self.e.configure(text = "You cannot follow yourself ")
			elif(self.d[0] in followers):
				self._toggle_state(self.e,'disabled')
				self.e.configure(text = "You already follow "+self.unames[0])


		# self.unames = list(sum(self.unames, ()))
		# entry = {}
		# label = {}

		# i = 0
		# for name in self.unames:
		# 	e = tk.Button(self.searchpage.frame,text = 'Follow')
		# 	e.grid(sticky='w')
		# 	entry[name] = e

		# 	lb = tk.Label(self.searchpage.frame, text=name, bg = 'white')
		# 	lb.grid(row=i, column=1)
		# 	label[name] = lb
		# 	i += 1
		# for i in uid :
		# 	self.sql1 = 'SELECT username from user where uid = %s'
		# 	self.fusername = self.mc.execute(self.sql1 % i)
		# 	self.fuser = self.mc.fetchall()
		# 	self.fuser = list(sum(self.fuser, ()))
		# 	self.fuserli.append(self.fuser)

		# print(self.fuserli)
		# msg = ''
		# for i in self.fuserli :
		# 	for j in self.fuserli[self.fuserli.index(i)]:
		# 		print(i)
		# 		msg = msg + i + '\n'

		# self.searchpage.searches.configure(text = 'msg')

	# def presssearchbutton3(self):
	# 	self.fusername = self.dmpage.searchuser_entry.get()
	# 	sql = 'SELECT username from user where username like "%s"'
	# 	self.mc.execute(sql % ("%"+self.fusername+"%"))
	# 	self.unames = self.mc.fetchall()
	# 	self.unames = list(sum(self.unames, ()))
	# 	entry = {}
	# 	label = {}

	# 	i = 0
	# 	for name in self.unames:
	# 		e = tk.Button(self.dmpage.frame,text = 'Follow')
	# 		e.grid(sticky='w')
	# 		entry[name] = e

	# 		lb = tk.Label(self.dmpage.frame, text=name, bg = 'white')
	# 		lb.grid(row=i, column=1)
	# 		label[name] = lb
	# 		i += 1
	def pressfollowbutton(self):
		# sql = 'SELECT uid from user where username = "%s"'
		# self.mc.execute(sql % self.fusername)
		# self.d = self.mc.fetchall()
		# self.d = list(sum(self.d, ()))

		sql = 'INSERT into friends(uid,fuid) values(%s,%s)'
		args=(self.uid,self.d[0])
		self.mc.execute(sql ,args)
		self.mydb.commit()
		self._toggle_state(self.e,'disabled')
		self.e.configure(text = "You are following %s"%(self.fusername))

	def pressaddpostbutton(self):
		self.addpostpage = AddPostPage.AddPostPage(self)

	def pressaddpostbutton1(self):
		self.filepath = ''
		self.filepath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
		self.addpostpage = AddPostPage.AddPostPage(self)
		try:
			img =tk.PhotoImage(file = self.filepath)
			# if im.shape[0]>300:
			# 	image = cv2.resize(image, (600,300), interpolation = cv2.INTER_AREA)
			# self.newlabel = tk.Canvas(self.addpostpage.filelabel,width = 1000,height = 1000,bg='red')
			# self.newlabel.pack()
		except (tk.TclError):
			self.addpostpage.filelabel.configure(text = 'Please Upload a image png File.',fg = 'red')
		else:
			self.addpostpage.filelabel.configure(image = img)
		self.mainloop()
		#self.addpostpage.filelabel.configure(image = image)

	def pressnotificationsbutton(self):
		self.notificationspage = NotificationsPage.NotificationsPage(self)
		self.notifications()

	def pressmyprofilebutton(self):
		self.navbar = LowerNavbar.Lowernavbar(self)
		self.myprofilepage = MyProfilePage.MyProfilePage(self)
		self.mc = self.connecttodatabase()
		self.mc.execute("Select count(uid) from friends where uid = %s "%(self.uid))
		self.following = self.mc.fetchall()
		self.following = list(sum(self.following, ()))
		self.myprofilepage.followingnumber.configure(text = self.following[0])

		self.mc.execute("Select count(fuid) from friends where fuid = %s "%(self.uid))
		self.followers = self.mc.fetchall()
		self.followers = list(sum(self.followers, ()))
		self.myprofilepage.followernumber.configure(text = self.followers[0])

		self.mc.execute("Select count(uid) from posts where uid = %s "%(self.uid))
		self.post = self.mc.fetchall()
		self.post = list(sum(self.post, ()))
		self.myprofilepage.postnumber.configure(text = self.post[0])

		self.myprofilepage.username1label.configure(text = self.username)
		print(self.uid)
		sql = "SELECT imgs from posts where uid = %s"
		args = (self.uid)
		self.mc.execute(sql,args)
		self.mydb.commit()
		self.image = self.mc.fetchall()
		self.image = list(sum(self.image, ()))
		self.index = 0
		if len(self.image)>0:
			self.nextpost()
		else:
			self._toggle_state(self.myprofilepage.nextbutton,'disabled')
			self._toggle_state(self.myprofilepage.prevbutton,'disabled')
			self.myprofilepage.imagelabel.configure(text = 'No Images Upload from Add Post Page.')
			
	def nextbutton(self):
		self._toggle_state(self.myprofilepage.prevbutton,'enabled')
		self.index+=1
		self.nextpost()
		

	def prevbutton(self):
		self._toggle_state(self.myprofilepage.nextbutton,'enabled')
		self.index-=1
		self.prevpost()
		

	def nextpost(self):
		if(self.index<=len(self.image)-1 and self.index>=0):
			image = io.imread(self.image[self.index])
			if image.shape[0]>300:
				image = cv2.resize(image, (600,300), interpolation = cv2.INTER_AREA)
			image = Image.fromarray(image)
			image = ImageTk.PhotoImage(image)
			self.myprofilepage.imagelabel.configure(image = image)
			self.mainloop()
		elif self.index<0:
			self._toggle_state(self.myprofilepage.nextbutton,'disabled')
			self.myprofilepage.imagelabel.configure(image = '',text = 'Press Next once more',fg = 'red')
		else:
			self._toggle_state(self.myprofilepage.nextbutton,'disabled')
			self.myprofilepage.imagelabel.configure(image = '',text = 'No More Images,Press Previous',fg = 'red')

	def prevpost(self):
		if(self.index>=0 and self.index<=len(self.image)-1):
			image = io.imread(self.image[self.index])
			if image.shape[0]>300:
				image = cv2.resize(image, (600,300), interpolation = cv2.INTER_AREA)
			image = Image.fromarray(image)
			image = ImageTk.PhotoImage(image)
			self.myprofilepage.imagelabel.configure(image = image)
			self.mainloop()
		elif self.index>len(self.image)-1:
			self._toggle_state(self.myprofilepage.prevbutton,'disabled')
			self.myprofilepage.imagelabel.configure(image = '',text = 'Press Previous once more',fg = 'red')
		else:
			self._toggle_state(self.myprofilepage.prevbutton,'disabled')
			self.myprofilepage.imagelabel.configure(image = '',text = 'No More Images,Press Next',fg = 'red')







		#self.myprofilepage.imagepost_frame.configure(image = img)
		# self.image = self.mc.fetchall()
		# self.image = list(sum(self.image,()))
		# print(len(self.image))

		# data = {}
		# button = {}
		# i = 0
		# for image in self.image:

		# 	with open(image, 'wb') as file:
		# 		file.write(data[i])

		# 	data[i] = tk.PhotoImage(data = image)
		# 	i = i+1

		# 	e = tk.Button(self.myprofilepage.imagepost_frame,text = 'Button',height = 200,width = 220, image = data[i])
		# 	e.grid(row = 0,column = i,columnspan = 30,rowspan = '10',padx = 10,pady = 10)
		# 	button[i] = e

		# with open(filename, 'wb') as file:
		# 	file.write(data)
		# self.myprofilepage.image_button.configure(image = )


	def presslogoutbutton(self):
		self.loginpage = Login_page.Login_page(self)

	def presseditprofilebutton(self):
		self.editprofile = EditProfile.EditProfile(self)

	def presschangeusernamebutton(self):
		self.changeusername = ChangeUsername.ChangeUsername(self)

	def presschangepasswordbutton(self):
		self.enterpassword = EnterPassword.EnterPassword(self)
		# self.changepassword = ChangePassword.ChangePassword(self)

	def presschangepasswordbutton2(self):
		password = self.enterpassword.enterpassword_entry.get()
		sql = "SELECT passwd from auth where uid = %s"
		self.mc.execute(sql % self.uid) 
		result = self.mc.fetchall()
		result = sum(result,())
		print(result)
		if password == result[0]:
			self.editprofile = EditProfile.EditProfile(self)
			self.changepassword = ChangePassword.ChangePassword(self)
		else : 
			self.enterpassword.msg_label.configure(text = "Incorrect Password",fg = "red")

	def pressmessagebutton(self):
		self.dmpage = DM_Page.DM_Page(self)	

	def myprofilebutton1(self):
		self.myprofile = MyProfilePage.MyProfilePage(self)

	# def pressreceivebutton(self):
	# 	self.pressmessagebutton1()

	def pressmessagebutton1(self):
		self.chat = Chat.Chat(self)
		sql = "SELECT uid from user where username = '%s'"
		self.mc.execute(sql % self.fusername)
		self.r = self.mc.fetchall() 
		self.r = list(sum(self.r , ()))

		sql1 = "SELECT msg from msgs where uid = %s AND fuid = %s"
		args = (self.uid,self.r)
		self.mc.execute(sql1,args)
		messages = self.mc.fetchall()
		messages = list(sum(messages,()))

		sql1 = "SELECT mid from msgs where uid = %s AND fuid = %s"
		args = (self.uid,self.r)
		self.mc.execute(sql1,args)
		myid = self.mc.fetchall()
		myid = list(sum(myid,()))
		myuid = []
		for i in range(len(myid)):
			myuid.append(self.uid)
		# print(myuid)
		# print(messages)
		# print(myid)

		me = list(map(list,zip(myuid,myid,messages)))
		# print(me)

		sql2 = "SELECT msg from msgs where uid = %s AND fuid = %s"
		self.mc.execute(sql2 % (self.r[0],self.uid))
		messages1 = self.mc.fetchall()
		messages1 = list(sum(messages1,())) 
		# print(messages1)

		sql2 = "SELECT mid from msgs where uid = %s AND fuid = %s"
		self.mc.execute(sql2 % (self.r[0],self.uid))
		myid1 = self.mc.fetchall()
		myid1 = list(sum(myid1,())) 
		fuid = []
		for i in range(len(myid1)):
			fuid.append(self.r[0])
		# print(fuid)
		# print(messages1)
		# print(myid1)

		her = list(map(list,zip(fuid,myid1,messages1)))
		# print(her)

		z = me + her
		z = sorted(z,key=lambda l:l[1])
		# print(z)
		if len(z) > 7:
			z = z[-7:len(z)]

		j = 0.05
		k = 0.08
		for m in z:
			if m[0] == self.r[0]:
				self.label_from = tk.Label(self.chat.mid_frame,bg = "black",fg = "white",text = m[2])
				self.label_from.place(relwidth = 0.3,relheight = 0.07,relx = 0.08,rely = k)
				j+=0.14
				k+=0.09
			else :
				self.label_to = tk.Label(self.chat.mid_frame,bg = "black",fg = "white",text = m[2])
				self.label_to.place(relwidth = 0.3,relheight = 0.07,relx = 0.68,rely = j)
				j+=0.09
				k+=0.14

		# i=0
		# d=0
		# j = 0.05
		# k = 0.1
		# for msg in messages:
		# 	self.label_to = tk.Label(self.chat.mid_frame,bg = "black",fg = "white",text = msg)
		# 	self.label_to.place(relwidth = 0.3,relheight = 0.07,relx = 0.68,rely = j)

		# 	if(len(messages1) > i ):
		# 		self.label_from = tk.Label(self.chat.mid_frame,bg = "black",fg = "white",text = messages1[d])
		# 		d+=1
		# 		self.label_from.place(relwidth = 0.3,relheight = 0.07,relx = 0.08,rely = k)
		# 	else:
		# 		pass

		# 	i += 1
		# 	j += 0.1
		# 	k += 0.1

	def pressbackbutton(self):
		self.navbar = LowerNavbar.Lowernavbar(self)
		self.dmpage= DM_Page.DM_Page(self)
		#self.lowernavbar = LowerNavbar.Lowernavbar(self)

	def presssearchbutton3(self):
		# print("Hiis")
		# self.fusername = self.dmpage.searchuser_entry.get()
		# sql = 'SELECT username from user where username = "%s"'
		# self.mc.execute(sql % self.fusername)
		# self.unames = self.mc.fetchall()
		# self.unames = list(sum(self.unames, ()))
		# entry = {}
		# j = 0.05
		# for name in self.unames:
		# 	self.e = tk.Button(self.dmpage.frame,text = name,bg = "black",fg = "white",command = self.pressmessagebutton1)
		# 	self.e.place(relheight = 0.1,relwidth = 1,rely = j)
		# 	entry[name] =self.e
		# 	j += 0.12
		##
		self.fusername = self.dmpage.searchuser_entry.get()
		sql = 'SELECT username from user where username = "%s"'
		self.mc.execute(sql % self.fusername)
		self.unames = self.mc.fetchall()
		self.unames = list(sum(self.unames, ()))
		entry = {}
		i = 0
		j = 0.05
		helv36 = tk.font.Font(family='Helvetica', size=30, weight='bold')
		for name in self.unames:
			self.e = tk.Button(self.dmpage.frame,font = helv36,text = "Message "+self.unames[i],bg = "black",fg = "white",command = self.pressmessagebutton1)
			self.e.place(relheight = 0.1,relwidth = 1,rely = j)
			entry[name] =self.e
			j += 0.12
			i += 1

		# sql = 'SELECT fuid from friends where uid = (SELECT uid from user where username = "%s")'
		# self.mc.execute(sql % self.username)
		# followers = self.mc.fetchall()
		# followers = list(sum(followers, ()))
		# print(followers)
		sql = 'SELECT uid from user where username = "%s"'
		self.mc.execute(sql % self.fusername)
		self.d = self.mc.fetchall()
		self.d = list(sum(self.d, ()))
		if(len(self.d) == 0):
			self.e1 = tk.Button(self.dmpage.frame,font = helv36,text = "No Users Found",bg = "black",fg = "white")
			self.e1.place(relheight = 0.1,relwidth = 1,rely = 0.05)
			# self.e1.configure(text = "No Users Found ")
		# else:
		# 	print(self.d[0])
		# 	print(self.uid)
		# 	if(self.d[0] == self.uid):
		# 		self._toggle_state(self.e,'disabled')
		# 		self.e.configure(text = "You cannot follow yourself ")
		# 	elif(self.d[0] in followers):
		# 		self._toggle_state(self.e,'disabled')
		# 		self.e.configure(text = "You already follow "+self.unames[0])


	def presssendbutton(self):
		self.msg = self.chat.message_entry.get()
		if(self.msg=='' or self.msg == 'Enter here'):
			self.chat.message_entry.configure(text = 'Enter here')
		else:
			sql = "INSERT into msgs(uid,fuid,msg) values(%s,%s,'%s')"
			args = (self.uid,self.r[0],self.msg)
			self.mc.execute(sql%args)
			self.mydb.commit()
			self.pressmessagebutton1()

	#def presschangeprofilepicturebutton(self):
	#	self.changeprofilepicture = ChangeProfilePicture.ChangeProfilePicture(self)

	def presschangeusernamebutton1(self):
		newusername = self.changeusername.newusername_entry.get()
		if self.username == newusername:
			self.editprofile = EditProfile.EditProfile(self)
			self.editprofile.usernamechangesuccessful_label.configure(text = "Entered username is the same as before",fg = "red")
		else:
			sql = "UPDATE user set username = '%s' where username = '%s'"
			args = (newusername,self.username)
			self.mc.execute(sql % args)
			self.mydb.commit()
			self.username = newusername
			self.editprofile = EditProfile.EditProfile(self)
			self.editprofile.usernamechangesuccessful_label.configure(text = "Username changed successfully",fg= "green")

	def presschangepasswordbutton1(self): 
		newpassword = self.changepassword.newpassword_entry.get()
		confirmpassword = self.changepassword.confirmpassword_entry.get()
		flag = 0
		if newpassword == '':
			self.changepassword.changepasswordunsuccessful_label.configure(text = "Password cannot be empty.",fg = "red")
		else:
			if newpassword == confirmpassword:
				sql = "UPDATE auth set passwd = '%s' where uid = %s"
				args = (confirmpassword,self.uid)
				self.mc.execute(sql %args)
				self.mydb.commit()
				self.editprofile = EditProfile.EditProfile(self)
				self.editprofile.usernamechangesuccessful_label.configure(text = "Password changed successfully",fg= "green")
			else:
				self.changepassword.newpassword_entry.configure(text = "")
				self.changepassword.confirmpassword_entry.configure(text = "") 
				self.changepassword.changepasswordunsuccessful_label.configure(text = "Passwords doesn't match.",fg = "red")

	def pressmessagebutton(self):
		self.dmpage = DM_Page.DM_Page(self)

	def pressnextbutton(self):
		if self.filepath == '':
			pass
		else :
			self.addcaptionpage = AddCaptionPage.AddCaptionPage(self)
			img =tk.PhotoImage(file = self.filepath)
			self.addcaptionpage.imagelabel.configure(image = img)
			self.mainloop()

	# def presschangeprofilepicturebutton(self):
	# 	self.mc = self.connecttodatabase()
	# 	self.mc.execute('SELECT uid from profile')

	# 	uids = self.mc.fetchall()
	# 	uids=list(sum(uids, ()))
	# 	print(uids)

	# 	self.profilepath = ''
	# 	self.profilepath = filedialog.askopenfilename()
	# 	try:
	# 		img =tk.PhotoImage(file = self.profilepath)
	# 	except (tk.TclError):
	# 		self.myprofilepage.profilepic.configure(text = 'Please Upload a image png File.',fg = 'red')
	# 	else:
	# 		self.myprofilepage = MyProfilePage.MyProfilePage(self)
	# 		self.myprofilepage.profilepic.configure(image = img)
	# 		root.mainloop()



	def upload(self):
		self.cap = self.addcaptionpage.captionbox.get()

		sql = "SELECT pid from posts"
		self.mc.execute(sql)

		pids = self.mc.fetchall()
		pids = list(sum(pids, ()))
		if len(pids)==0:
			pid = 0
		else:
			pid = max(pids)
			pid+=1

		config = {
		"apiKey": "AIzaSyBpHBfhyDCJPD_iXFGbR1zD9K0wyduh4rE",
		"authDomain": "kilogramlikeinstagram.firebaseapp.com",
		"databaseURL": "https://kilogramlikeinstagram.firebaseio.com",
		"projectId": "kilogramlikeinstagram",
		"storageBucket": "kilogramlikeinstagram.appspot.com",
		"messagingSenderId": "334961156944"
		}
		firebase = pyrebase.initialize_app(config)
		storage = firebase.storage()
		storage.child("images/%s.png"%(pid)).put(self.filepath)
		uploadurl = storage.child("images/%s.png"%(pid)).get_url(None)

		sql = "INSERT into posts values(%s,%s,%s,%s,%s)"
		args=(self.uid,pid,uploadurl,self.uid,self.cap)
		self.mc.execute(sql,args)
		self.mydb.commit()
		self.pressmyprofilebutton()

	def friendchat_profile(self):
		self.navbar = LowerNavbar.Lowernavbar(self)
		self.myprofilepage = MyProfilePage.MyProfilePage(self)
		self.mc = self.connecttodatabase()
		self.mc.execute("Select count(uid) from friends where uid = %s "%(self.r[0]))
		self.following = self.mc.fetchall()
		self.following = list(sum(self.following, ()))
		self.myprofilepage.followingnumber.configure(text = self.following[0])

		self.mc.execute("Select count(fuid) from friends where fuid = %s "%(self.r[0]))
		self.followers = self.mc.fetchall()
		self.followers = list(sum(self.followers, ()))
		self.myprofilepage.followernumber.configure(text = self.followers[0])

		self.mc.execute("Select count(uid) from posts where uid = %s "%(self.r[0]))
		self.post = self.mc.fetchall()
		self.post = list(sum(self.post, ()))
		self.myprofilepage.postnumber.configure(text = self.post[0])

		self.mc.execute("SELECT username from user where uid = %s"%(self.r[0]))
		self.friendname = self.mc.fetchall()
		self.myprofilepage.username1label.configure(text = self.friendname)
		self.myprofilepage.edit_button.configure(state = "disabled",bg = "white",bd = 0)
		self.myprofilepage.logout_button.configure(state = "disabled",bg = "white",bd = 0)

	def notifications(self):
		sql = "SELECT fid from friends where fuid = %s"
		args = (self.uid)
		self.mc.execute(sql%args)
		fid = self.mc.fetchall()
		fid = list(sum(fid,()))
		
		sql = "SELECT uid from friends where fuid = %s"
		args = (self.uid)
		self.mc.execute(sql%args)
		ffuid = self.mc.fetchall()
		ffuid = list(sum(ffuid,()))

		datauser = []
		for f in ffuid:
			sql = "SELECT username from user where uid = %s"
			args = (f)
			self.mc.execute(sql%args)
			fffuid = self.mc.fetchall()
			fffuid = list(sum(fffuid,()))
			datauser+=fffuid

		sql = "SELECT fid from friends where uid = %s"
		args = (self.uid)
		self.mc.execute(sql%args)
		fid1 = self.mc.fetchall()
		fid1 = list(sum(fid1,()))
		
		sql = "SELECT fuid from friends where uid = %s"
		args = (self.uid)
		self.mc.execute(sql%args)
		ffuid1 = self.mc.fetchall()
		ffuid1 = list(sum(ffuid1,()))

		datauser2 = []
		for f in ffuid1:
			sql = "SELECT username from user where uid = %s"
			args = f
			self.mc.execute(sql,args)
			fffuid = self.mc.fetchall()
			fffuid = list(sum(fffuid,()))
			datauser2+=fffuid
	
		friends = list(map(list,zip(fid,ffuid,datauser)))
		friends1 = list(map(list,zip(fid1,ffuid1,datauser2)))
		print(friends)
		print(friends1)

		
		j = 0.05
		for k in friends:
			label = tk.Label(self.notificationspage.following_frame,bg = "white", fg = "black",text = "%s started following you!" % k[2])
			label.place(relwidth = 0.8,relheight = 0.05,relx = 0.1, rely = j)
			j+=0.05

	
		for k in friends1:
			label = tk.Label(self.notificationspage.followed_frame,bg = "white", fg = "black",text = "You started following %s!" % k[2])
			label.place(relwidth = 0.8,relheight = 0.05,relx = 0.1, rely = j)
			j+=0.05

		sql = "SELECT mid from msgs where fuid = %s"
		args = (self.uid)
		self.mc.execute(sql%args)
		fid = self.mc.fetchall()
		fid = list(sum(fid,()))	
		
		sql = "SELECT uid from msgs where fuid = %s" #the uids from which i received the messages
		args = (self.uid)
		self.mc.execute(sql%args)
		ffuid = self.mc.fetchall()
		ffuid = list(sum(ffuid,()))

		datauser = []
		for f in ffuid:
			sql = "SELECT username from user where uid = %s"
			args = (f)
			self.mc.execute(sql%args)
			fffuid = self.mc.fetchall()
			fffuid = list(sum(fffuid,()))
			datauser+=fffuid

		message = []
		for f in ffuid:
			sql = "SELECT msg from msgs where fuid = %s"
			args = (self.uid)
			self.mc.execute(sql%args)
			messages = self.mc.fetchall()
			messages = list(sum(messages,()))

		friends = list(map(list,zip(fid,ffuid,datauser,messages)))
		j = 0.05
		friends = friends[-7:len(friends)]
		for k in friends:
			label = tk.Label(self.notificationspage.message_frame,bg = "white", fg = "black",text = "%s has sent you a message." % (k[2]))
			label.place(relwidth = 0.8,relheight = 0.05,relx = 0.1, rely = j)
			j+=0.05
			
			

# disconnect krtoy me tula


if __name__=='__main__':
	# info = AppKit.NSBundle.mainBundle().infoDictionary()
	# info['LSUIElement'] = True

	root = tk.Tk()
	r = Root(root)
	# r._toggle_state(r.loginpage.kilogramlabel,'disabled')
	r.mainloop()