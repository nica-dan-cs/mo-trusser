#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import *
from material_manager import *
from window_grinda import *
from window_placa import *
from areas_n_masses import *
from concrete_resistance_n_deformation import *


init_areas_n_masses()
init_concrete_resistance_n_deformation()
load_all_metals()

main_menu = Tk()
main_menu.wm_title("mo-trusser v 0.1")

nb = Notebook(main_menu)
nb.add(window_placa(500,500).retrieve_frame(),text="Placa")
nb.add(window_grinda(500,500).retrieve_frame(),text="Grinda - camp(T)")



nb.pack()
main_menu.mainloop()
