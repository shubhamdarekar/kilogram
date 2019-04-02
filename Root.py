# import AppKit
import tkinter as tk
import Login_page
import Signup
import test
import LowerNavbar
import pymysql
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
		self.mydb = pymysql.connect(host="127.0.0.1",user="root",passwd="",db="kilogram")
		self.mc = self.mydb.cursor()
		return self.mc

	def insertinUser(self, cursor,fname,lname,age,phnno,emailid,username ):
		cursor.execute('INSERT into user (fname,lname,age,phoneNo,emailid,username) values ("%s","%s","%s","%s","%s,"%s")'%(fname,lname,age,phnno,emailid,username))
		cursor.commit()

	
	def clickcancel(self):
		self.master.destroy()

	def clickEscape(self,event):
		self.master.destroy()

	def _toggle_state(self,widget,state):
		state = state if state in ('normal','disabled') else 'normal'
		widget.configure(state = state)

	def presssignup(self):
		self.signuppage = Signup.Signup_page(self)

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
		if fname == '' or lname == '' or email == '' or phnno == '' or password == '' or cnfpassword == '':
			if fname == '':
				self.signuppage.firstnameempty.configure(text = 'First name Cannot be Empty!!!')
			if lname == '':
				self.signuppage.lastnameempty.configure(text = 'Last name Cannot be Empty!!!')
			if email == '':
				self.signuppage.emailempty.configure(text = 'Email Address Cannot be Empty!!!')
			if phnno == '':
				self.signuppage.phonenoempty.configure(text = 'Phone number Cannot be Empty!!!')
			if username == '':
				self.signuppage.usernameempty.configure(text = 'Username number Cannot be Empty!!!')
			if password == '':
				self.signuppage.passwordempty.configure(text = 'Password Cannot be Empty!!!')
			if cnfpassword == '':
				self.signuppage.confirmpasswordempty.configure(text = 'This field Cannot be Empty!!!')
		else :
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
					self.mc.execute('INSERT into user (fname,lname,age,phoneNo,emailid,username) values ("%s","%s",%s,"%s","%s","%s")'%(fname,lname,age,phnno,email,username))
					self.mydb.commit()
					self.mc.execute('SELECT uid from user where username = "%s"'%(username))
					self.uidli = self.mc.fetchall()
					self.uidli = list(sum(self.uidli,()))
					self.mc.execute('INSERT into auth (uid,passwd) values (%s,"%s")'%(self.uidli[0],password))
					self.mydb.commit()
					self.loginpage = Login_page.Login_page(self)
					self.loginpage.loginsuccesslabel.configure(text = 'Signup successfull!!!')


				
	

	def presslogin(self):
		self.loginpage = Login_page.Login_page(self)


	def presslogin1(self):
		username = self.loginpage.usernameentry.get()
		password = self.loginpage.passwordentry.get()

		if username =='' or password == '':
			flag = 0
			if username == '':
				self.loginpage.usernameempty.configure(text = 'Username Cannot be empty!!!')
				self.loginpage.passwordempty.configure(text = '')
				flag = 1
			if password == '':
				self.loginpage.passwordempty.configure(text = 'Password Cannot be empty!!!')
				if flag == 0 : self.loginpage.usernameempty.configure(text = '')
		else:
			self.loginpage.usernameempty.configure(text = '')
			self.loginpage.passwordempty.configure(text = '')
			self.mc = self.connecttodatabase()
			self.mc.execute("select username from user")
			self.usernameli = self.mc.fetchall()
			self.usernameli = list(sum(self.usernameli, ()))
			if username not in self.usernameli :
				self.loginpage.usernameempty.configure(text = 'The Username Entered is wrong.')
			else:
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
					self.loggedin = LowerNavbar.Lowernavbar(self)
				else :
					self.loginpage.passwordempty.configure(text = 'Password is incorrect!!!')




if __name__=='__main__':
	# info = AppKit.NSBundle.mainBundle().infoDictionary()
	# info['LSUIElement'] = True

	root = tk.Tk()
	r = Root(root)
	#r._toggle_state(r.loginpage.kilogramlabel,'disabled')
	r.mainloop()
			