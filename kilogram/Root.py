import tkinter as tk
class Root:
	
	@staticmethod
	def create_window():
		global root
		global canvas
		root = tk.Tk()
		canvas = tk.Canvas(root,height=700,width=1080)
		canvas.pack()
r=Root()
r.create_window()
