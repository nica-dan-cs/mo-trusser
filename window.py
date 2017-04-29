from tkinter import *
from tkinter.ttk import *

class window:
	frame = None
	#test for global define of variable
	numb=0
	all_written={"Directie":[],"Pozitie":[],"Nr bare + ɸ ":[],"Mcap [kNm]":[],"ρ [‰]":[]}
	all_written_keys = ["Directie","Pozitie","Nr bare + ɸ ","Mcap [kNm]","ρ [‰]"]
	all_written_T_beam={"Denumire":[],"Nr bare + ɸ ":[],"Arie [mm2]":[],"Mcap [kNm]":[],"ρ [‰]":[]}
	all_written_T_beam_keys=["Denumire","Nr bare + ɸ ","Arie [mm2]","Mcap [kNm]","ρ [‰]"]
	all_written_double_beam={"Denumire":[],"Nr bare + ɸ ":[],"Arie [mm2]":[],"Mcap [kNm]":[],"ρ [‰]":[]}
	all_written_double_beam_keys=["Denumire","Nr bare + ɸ ","Arie [mm2]","Mcap [kNm]","ρ [‰]"]
	def __init__(self,width,height):
		self.frame = Frame(width=width,height=height)
		self.frame.pack()

	def retrieve_frame(self):
		return self.frame
