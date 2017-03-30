from tkinter import *
from tkinter.ttk import *

class window:
	frame = None

	def __init__(self,width,height):
		self.frame = Frame(width=width,height=height)
		self.frame.pack()

	def retrieve_frame(self):
		return self.frame