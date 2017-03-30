from window import *
from tkinter import *
from tkinter.ttk import *
from material_manager import *
from beton import *
from areas_n_masses import *

class window_grinda(window):

	tb_grosime = None
	tb_mcap = None
	tb_acoperire = None

	label_beton = None
	listbox_beton = None

	label_otel = None
	listbox_otel = None

	def __init__(self,width,height):

		window.__init__(self,width,height)

		#Grosime
		label = Label(self.frame,text="Grosime",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.05)
		self.tb_grosime = Text(self.frame,height=1,width=20)
		self.tb_grosime.pack()
		self.tb_grosime.place(rely=0.08)

		#Mcap
		label = Label(self.frame,text="Mcap",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.12)
		self.tb_mcap = Text(self.frame,height=1,width=20)
		self.tb_mcap.pack()
		self.tb_mcap.place(rely=0.15)

		#Acoperire
		label = Label(self.frame,text="Acoperire",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.19)
		self.tb_acoperire = Text(self.frame,height=1,width=20)
		self.tb_acoperire.pack()
		self.tb_acoperire.place(rely=0.22)

		#Beton
		self.label_beton = Label(self.frame, text="Beton: ",font=("Helvetica", 10))
		self.label_beton.pack()
		self.label_beton.place(rely=0.26)

		subframe = Frame(self.frame)
		subframe.pack(fill=X)
		subframe.place(rely=0.30)

		scrollbar_beton = Scrollbar(subframe,orient=VERTICAL)
		scrollbar_beton.pack(side=RIGHT,fill=Y)

		self.listbox_beton = Listbox(subframe,height=3,width=16,selectmode=BROWSE)
		self.listbox_beton.pack()
		self.listbox_beton.place()
		self.listbox_beton.config(yscrollcommand=scrollbar_beton.set)
		scrollbar_beton.config(command=self.listbox_beton.yview)

		for concrete_name in all_concrete_names:
			self.listbox_beton.insert(END,concrete_name)
		self.listbox_beton.bind("<<ListboxSelect>>",self.listbox_beton_callback)

		#Otel
		self.label_otel = Label(self.frame, text="Otel: ",font=("Helvetica", 10))
		self.label_otel.pack()
		self.label_otel.place(rely=0.4)

		subframe = Frame(self.frame)
		subframe.pack(fill=X)
		subframe.place(rely=0.45)

		scrollbar_otel = Scrollbar(subframe,orient=VERTICAL)
		scrollbar_otel.pack(side=RIGHT,fill=Y)

		self.listbox_otel = Listbox(subframe,height=3,width=16,selectmode=BROWSE)
		self.listbox_otel.pack()
		self.listbox_otel.place()
		self.listbox_otel.config(yscrollcommand=scrollbar_otel.set)
		scrollbar_otel.config(command=self.listbox_otel.yview)

		all_metals = load_all_metals()
		for metal in all_metals:
			self.listbox_otel.insert(END,metal.retrieve_name())
		self.listbox_otel.bind("<<ListboxSelect>>",self.listbox_otel_callback)

		#Run Button
		run_button = Button(self.frame,text="Process",command=self.run_button_callback)
		run_button.pack()
		run_button.place(rely=0.57)

	def listbox_otel_callback(self,unused):
		index_of_selected = self.listbox_otel.curselection()
		self.label_otel.config(text="Otel: " + str(self.listbox_otel.get(index_of_selected)))

	def listbox_beton_callback(self,unused):
		index_of_selected = self.listbox_beton.curselection()
		self.label_beton.config(text="Beton: " + str(self.listbox_beton.get(index_of_selected)))

	def run_button_callback(self):
		beton = self.label_beton['text']
		otel = self.label_otel['text']
		grosime = self.tb_grosime.get("1.0",END)
		mcap = self.tb_mcap.get("1.0",END)
		acoperire = self.tb_acoperire.get("1.0",END)

		output = self.process(beton,otel,grosime,mcap,acoperire)
		### Render output to user ###

	def process(self,beton,otel,grosime,mcap,acoperire):
		### Perform computations here ###
		print("self.process() not implemented yet")
