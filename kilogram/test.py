import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

#root.withdraw()

filepath = filedialog.askopenfilename()

print(filepath)