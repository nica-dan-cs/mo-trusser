#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import *
from material_manager import *
from window_grinda import *
from areas_n_masses import *
from concrete_resistance_n_deformation import *

init_areas_n_masses()
init_concrete_resistance_n_deformation()
load_all_metals()

main_menu = Tk()
main_menu.wm_title("mo-trusser v 0.1")

frame_placa = Frame(width=600,height=500)
frame_placa.pack(side=LEFT, fill=BOTH)

nb = Notebook(main_menu)
nb.add(window_grinda(800,500).retrieve_frame(),text="Grinda")
nb.add(frame_placa,text="Placa")
nb.pack()
main_menu.mainloop()

#all_metals = load_all_metals()
#print(all_metals)