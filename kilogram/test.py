import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root,height=700,width=1080)
canvas.pack()
screen1 = tk.Frame(canvas,bg="white")
screen1.place(relheight = 1,relwidth = 1)
navbarframe = tk.Frame(screen1,height = 70, width = 1080,bg = "black")
navbarframe.pack(side= 'bottom')
root.mainloop()