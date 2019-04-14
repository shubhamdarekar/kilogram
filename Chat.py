import tkinter as tk

class Chat(tk.Frame):
	def __init__(self,master):
		 main_frame = tk.Frame(master.canvas,bg = "white")
		 main_frame.place(relheight = 1,relwidth = 1)

		 upper_frame = tk.Frame(main_frame,bg = "black")
		 upper_frame.place(relwidth = 1,relheight = 0.1)

		 self.mid_frame = tk.Frame(main_frame,bg = "white")
		 self.mid_frame.place(relheight = 0.8,relwidth = 1,rely = 0.1)

		 self.back_button = tk.Button(upper_frame,bg = "black",fg = "white",font = ('bold',15),bd = 0,text = "Back",command = master.pressbackbutton)
		 self.back_button.place(relheight = 0.7,relwidth = 0.1,relx = 0.02,rely = 0.15)

		 username_button = tk.Button(upper_frame,text = master.fusername,fg = "white",bd = 0,bg = "black",font = ('bold',15),command = master.friendchat_profile)
		 username_button.place(relheight = 0.7,relwidth = 0.2,relx = 0.77,rely = 0.15)

		 lower_frame = tk.Frame(main_frame,bg = "white")
		 lower_frame.place(relwidth = 1,relheight = 0.1,rely = 0.9)

		 message_label = tk.Label(lower_frame,bg = "white",fg = "black",text = "Message",font = ('bold',20))
		 message_label.place(relheight = 0.9,relwidth = 0.1,relx = 0.05,rely = 0.02)

		 self.message_entry = tk.Entry(lower_frame,bg = "#ECECEC")
		 self.message_entry.place(relwidth = 0.6,relheight = 0.6,relx = 0.2,rely = 0.15)

		 send_button = tk.Button(lower_frame,bg = "black",fg = "white",font = ('bold',10),text = "Send",command = master.presssendbutton)
		 send_button.place(relheight = 0.6,relwidth = 0.07,relx = 0.805,rely = 0.078)

		 receive_button = tk.Button(lower_frame,bg = "black",fg = "white",font = ('bold',10),text = "Refresh to Recieve",command = master.pressmessagebutton1)
		 receive_button.place(relheight = 0.6,relwidth = 0.12,relx = 0.885,rely = 0.078)