from window import *
from tkinter import *
from tkinter.ttk import *
from material_manager import *
from beton import *
from areas_n_masses import *

class window_placa(window):

	### Define class wide variables here for anything that must be seen across multiple functions ###

	def __init__(self,width,height):

		window.__init__(self,width,height)

		### Define GUI here. Remember to also create callbacks for listboxes and buttons ###

	def run_button_callback(self):
		### Parse input data and send it to the process method ###
		print("self.run_button_callback() not implemented yet")

		output = self.process()
		### Render output to user ###

	def process(self):
		### Perform computations here ###
		print("self.process() not implemented yet")
