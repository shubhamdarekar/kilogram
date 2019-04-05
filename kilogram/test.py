import sqlite3
import pymysql
import os.path
from os import listdir, getcwd
from IPython.core.display import Image
from tkinter import filedialog
import tkinter as tk
import mysql.connector
import pickle
from PIL import Image
import request



mydb = pymysql.connect(host="192.168.1.9",user="root1",passwd="",db="projectdb")
conn= mydb.cursor()

filepath = filedialog.askopenfilename()
file = request.files['inputfile']

# with open(filepath, 'rb') as input_file:
# 	ablob = input_file.read()

img =Image.open( filepath)

# image = {
#     'pixels': img.tobytes(),
#     'size': img.size,
#     'mode': img.mode,
# }
ablob = open('pickl.pkl', 'wb')
pickle.dump(img,ablob)
print(ablob)
# base=os.path.basename(filepath)
# afile, ext = os.path.splitext(base)
sql = '''INSERT INTO tp
(img)
VALUES("%s");'''
conn.execute(sql%(pickl.pkl))

mydb.commit()
mydb.close()

mydb = mysql.connector.connect(host="192.168.1.9",user="root1",passwd="",db="projectdb")
conn= mydb.cursor()

sql = "SELECT img FROM tp WHERE id = '%s'"
# param = {'id': 0}
conn.execute(sql% '1')
ablob = [item[0] for item in conn.fetchall()]
im = open(ablob[0],'rb')
imm= pickle.load(im)
# filename = 'abc.png'
# with open(filename, 'wb') as output_file:
# 	output_file.write(ablob[0])
img = Image(filename = './'+filename)

root = tk.Tk()
imglabel = tk.Label(root,height = 100,image = img)
imglabel.pack()
root.mainloop()
