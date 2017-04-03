from window import *
from tkinter import *
from tkinter.ttk import *
from material_manager import *
from beton import *
from areas_n_masses import *
from otel import *
from math import *
from tkinter import messagebox
from heapq import nsmallest

class window_placa(window):

	### Define class wide variables here for anything that must be seen across multiple functions ###
	tb_grosime = None
	tb_mom = None
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
		label=Label(self.frame,text="cm",font=("Helvetica", 10))		
		label.pack()
		label.place(rely=0.08,relx=0.42)

		#Mom
		label = Label(self.frame,text="Moment",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.12)
		self.tb_mom = Text(self.frame,height=1,width=20)
		self.tb_mom.pack()
		self.tb_mom.place(rely=0.15)
		label=Label(self.frame,text="kNm",font=("Helvetica", 10))		
		label.pack()
		label.place(rely=0.15,relx=0.42)

		#Acoperire
		label = Label(self.frame,text="Acoperire",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.19)
		self.tb_acoperire = Text(self.frame,height=1,width=20)
		self.tb_acoperire.pack()
		self.tb_acoperire.place(rely=0.22)
		label=Label(self.frame,text="cm",font=("Helvetica", 10))		
		label.pack()
		label.place(rely=0.22,relx=0.42)

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

		all_metals = get_all_metals()
		for metal in all_metals:
			self.listbox_otel.insert(END,metal.retrieve_name())
		self.listbox_otel.bind("<<ListboxSelect>>",self.listbox_otel_callback)

		#Run Button
		run_button = Button(self.frame,text="Process",command=self.run_button_callback)
		run_button.pack()
		run_button.place(rely=0.57)


		### Define GUI here. Remember to also create callbacks for listboxes and buttons ###
	def listbox_otel_callback(self,unused):
		index_of_selected = self.listbox_otel.curselection()
		self.label_otel.config(text="Otel: " + str(self.listbox_otel.get(index_of_selected)))

	def listbox_beton_callback(self,unused):
		index_of_selected = self.listbox_beton.curselection()
		self.label_beton.config(text="Beton: " + str(self.listbox_beton.get(index_of_selected)))

	def run_button_callback(self):
		### Parse input data and send it to the process method ###
		beton_ales = beton(self.label_beton['text'].split(' ')[1])
		otel_ales = get_metal_by_names(self.label_otel['text'])
		grosime = self.tb_grosime.get("1.0",END)
		mom = self.tb_mom.get("1.0",END)
		acoperire = self.tb_acoperire.get("1.0",END)

		output = self.process(beton_ales,otel_ales,grosime,mom,acoperire)
		
		### Render output to user ###
	
	def process(self,beton,otel,grosime,mom,acoperire):
		### Perform computations here ###
		true=1
		h=float(grosime)*10
		b=1000
		fcd=(beton.fck)/1.5
		fyd=(otel.fyk)/1.15
		c=float(acoperire)*10
		d=h-(c+5)
		M=float(mom)*10**6
		if (2*M)/(b*fcd)>d**2:
			messagebox.showerror("Sa va fie Rusine","Moment prea mare pentru seciunea data \nx negativ \nSchimbati sectiunea")
			true=0
		
		x=d-sqrt(d**2-(2*M)/(b*fcd))
		
		if otel.comercial_name=="OB 37":
			x_lim=0.6*d
		elif otel.comercial_name=="PC 52" or otel.comercial_name=="PC 60":
			x_lim=0.55*d
		elif otel.comercial_name=="BST 500":
			x_lim=0.467*d

		if x>x_lim:
			messagebox.showinfo("Sa va fie Rusine","X mai mare ca x lim \nSchimbati sectiunea")
			true=0
		else:
			As=(b*x*fcd)/fyd
			print (As)
		
		if true==1:
			label=Label(self.frame,font=("Helvetica", 10))
			label.pack()
			label.place(rely=0.2,relx=0.5)
			label.config(text="x=" + str (round(x,2)/10) + " cm")

		

	
		matrix=[[0 for x in range(3)] for y in range(30)]
		p=0		
		for i in range (6,16,2):
			print ("phi=",i)			
			for nr in range (5,11):			
				print (area_by_phi(i,nr))
				matrix[p][0]=area_by_phi(i,nr)
				matrix[p][1]=i
				matrix[p][2]=nr
				p=p+1
				
		print ("stoooop")
		
		all_solutions = proper_closest(500,3)
		for s in all_solutions:
			print(s)

		
		def closest(number,matr):
			higher=[]
		
			for i in range(30):
				vect=[item[0] for item in matrix]
			for smth in vect:
				if smth>number:
					higher.append(smth)
			nsmallest(2,higher)
			return higher
				
			#higher.argsort()[-3:][::-1]
			
		
		print (closest(As,matrix))
		
		
