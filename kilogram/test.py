import tkinter as tk
from tkinter import filedialog
# import os
# def load_photo_tab_two(file_path):
# 	img = image_path(file_path)
# 	imglabel2.configure(image = img)
# 	imglabel2.image = img
# def select_image():
# 	path = filedialog.askopenfilename(initialdir = "/",title = "Select File",filetypes = (("PNGs","*.png"),("GIFs","*.gif"),("All Files","*.*")))

# 	try :
# 		if path :
# 			fname = os.path.basename(path)
# 			fnh = db_config.PHOTO_DIRECTORY + fname
# 			fcopy = path
# 			imgselected = True
# 			load_photo_tab_two(fcopy)

# 	except IOError as err:
# 		image_selected = False
# 		messagebox.showinfo("File Error", err)

# select_image()

# root = tk.Tk()

# # filepath = 'C:/Users/shubh/OneDrive/Desktop/download.png'
# filepath = filedialog.askopenfilename()
# # print(filepath)
# image =tk.PhotoImage(file = filepath)
# newlabel = tk.Label(root,image = image)
# newlabel.place(relwidth = 1,relheight = 1)

# filepath = filedialog.askopenfilename()
# #addpostpage = AddPostPage.AddPostPage(
# img =tk.PhotoImage(file = filepath)
# print(img)
# newlabel = tk.Canvas(root,width = 1000,height = 1000,bg='red')
# newlabel.pack()
# newlabel.create_image(20,20,anchor = 'nw',image = img)

# root.mainloop()


# from tkinter import *
# import datetime

# root = Tk()

# lab = Label(root)
# lab.pack()

# def clock():
#     time = datetime.datetime.now().strftime("Time: %H:%M:%S")
#     lab.config(text=time)
#     #lab['text'] = time
#     root.after(1000, clock) # run itself again after 1000 ms

# # run first time
# clock()

# root.mainloop()
global filepath
p=(filepath == None)
print(p)