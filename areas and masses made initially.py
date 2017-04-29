from window import *
from tkinter import *
from tkinter.ttk import *
from material_manager import *
from beton import *
from areas_n_masses import *
from otel import *
from math import *
from tkinter import messagebox
from utils import *

class window_grinda_dubla(window):

	### Define class wide variables here for anything that must be seen across multiple functions ###
	tb_inaltime = None
	tb_latime = None
	tb_grosime_placa=None
	tb_arie=None
	tb_phi=None
	tb_mom = None
	tb_computations=None
	tb_name=None
	
	
	label_beton = None
	listbox_beton = None

	label_otel = None
	listbox_otel = None
	
	to_be_written_csv={}
	label_display = []
	radio_button=[]
	var_selected=""
	var=None

	def __init__(self,width,height):

		window.__init__(self,width,height)		
		
		#Inaltime	
		label = Label(self.frame,text="Inaltime(h)                 cm",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.01)
		self.tb_inaltime = Text(self.frame,height=1,width=20)
		self.tb_inaltime.pack()
		self.tb_inaltime.place(rely=0.04)
		

		#Latime
		label = Label(self.frame,text="Latime(b)                   cm",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.08)
		self.tb_latime = Text(self.frame,height=1,width=20)
		self.tb_latime.pack()
		self.tb_latime.place(rely=0.11)
		
		#Grosime placa
		label = Label(self.frame,text="Grosime placa           cm",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.15)
		self.tb_grosime_placa = Text(self.frame,height=1,width=20)
		self.tb_grosime_placa.pack()
		self.tb_grosime_placa.place(rely=0.18)

		#Arie
		label = Label(self.frame,text="Arie (As')                mm2",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.22)
		self.tb_arie = Text(self.frame,height=1,width=20)
		self.tb_arie.pack()
		self.tb_arie.place(rely=0.25)
		
		#Phi
		label = Label(self.frame,text="Phi                          mm",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.29)
		self.tb_phi = Text(self.frame,height=1,width=20)
		self.tb_phi.pack()
		self.tb_phi.place(rely=0.32)



		#Mom
		label = Label(self.frame,text="Moment                  kNm",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.36)
		self.tb_mom = Text(self.frame,height=1,width=20)
		self.tb_mom.pack()
		self.tb_mom.place(rely=0.39)

		
		
	
		#Beton
		self.label_beton = Label(self.frame, text="Beton: ",font=("Helvetica", 10))
		self.label_beton.pack()
		self.label_beton.place(rely=0.43)

		subframe = Frame(self.frame)
		subframe.pack(fill=X)
		subframe.place(rely=0.46)

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
		self.label_otel.place(rely=0.56)

		subframe = Frame(self.frame)
		subframe.pack(fill=X)
		subframe.place(rely=0.59)

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
		
		#Number of computations
		label = Label(self.frame,text="Numar de combinatii",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.69)
		self.tb_computations = Text(self.frame,height=1,width=20)
		self.tb_computations.pack()
		self.tb_computations.place(rely=0.72)
		self.tb_computations.insert(END,"7")
		
		#Name
		label = Label(self.frame,text="Denumire:",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.76)
		self.tb_name = Entry(self.frame,width=18)
		self.tb_name.pack()
		self.tb_name.place(rely=0.79)

		

		#Run Button
		run_button = Button(self.frame,text="Process",command=self.run_button_callback)
		run_button.pack()
		run_button.place(rely=0.83,relx=0.06)
		
		#Add to file  Button
		add_to_file_button = Button(self.frame,text="Add to file",command=self.add_to_file_button_callback)
		add_to_file_button.pack()
		add_to_file_button.place(rely=0.89,relx=0.06)
		
		#Create file Button
		create_file_button = Button(self.frame,text="Create File",command=self.create_file_callback)
		create_file_button.pack()
		create_file_button.place(rely=0.95,relx=0.06)
		
	
		
		
	
		### Define GUI here. Remember to also create callbacks for listboxes and buttons ###
	def listbox_otel_callback(self,unused):
		index_of_selected = self.listbox_otel.curselection()
		self.label_otel.config(text="Otel: " + str(self.listbox_otel.get(index_of_selected)))

	def listbox_beton_callback(self,unused):
		index_of_selected = self.listbox_beton.curselection()
		self.label_beton.config(text="Beton: " + str(self.listbox_beton.get(index_of_selected)))
	

	def run_button_callback(self):
		### Parse input data and send it to the process method ###
		try:
			beton_ales = beton(self.label_beton['text'].split(' ')[1])
			otel_ales = get_metal_by_names(self.label_otel['text'])
			inaltime = float(self.tb_inaltime.get("1.0",END))
			latime = float(self.tb_latime.get("1.0",END))
			grosime_placa=float(self.tb_grosime_placa.get("1.0",END))
			arie=float(self.tb_arie.get("1.0",END))
			phi=float(self.tb_phi.get("1.0",END))
			mom = float(self.tb_mom.get("1.0",END))
		except:
			messagebox.showerror("Invalid input","    ERROR     ")
			return
			
		computations=None	
		try:
			computations=float(self.tb_computations.get("1.0",END))
		except:
			computations=float(7)
		

		output = self.process(beton_ales,otel_ales,inaltime,latime,grosime_placa,arie,phi,mom,computations)
	
		### Render output to user ###

		#creates the file with all requested data
	def create_file_callback(self):
		return dictionary_to_csv(self.all_written_T_beam,self.all_written_T_beam_keys,"armare_grinda_camp.csv")

	def add_to_file_button_callback(self):
		name=[]
		
		name.append(self.tb_name.get())
		
		if name==['']:
			name=["none"]	
		
		
		output=self.add_to_file(name) #variables defined here --> made them available in add_to_file function
		

		#function for radio button - #gets the variable from radio button - and returns its value
	def selected (self):
		self.var_selected=self.var.get()
	
		#append to all_written_T_beam every chosen option along all processes made	
	def add_to_file(self,name):
		ceva=[]
		try:
			for h in self.to_be_written_csv:
				if float(h)==float(self.var_selected):
					for smth in self.to_be_written_csv[h]:
						ceva.append(smth)
		except:
			messagebox.showerror("Eroare","Selectati o optiune")
		
		self.all_written_T_beam["Denumire"].append(str(location).strip("['']"))				
		self.all_written_T_beam["Nr bare"].append(ceva[0])
		self.all_written_T_beam["ɸ"].append(int(ceva[1]))
		self.all_written_T_beam["Mcap [kNm]"].append(round(ceva[2],2))
		self.all_written_T_beam["ρ [‰]"].append(round(ceva[3]*1000,3))
		
		

	def process(self,beton,otel,inaltime,latime,grosime_placa,arie,phi,mom,computations):
		#clears the labels
		for l in self.label_display:
			l.place_forget()
		
	 	#destroys radio buttons
		for l in self.radio_button:
			l.destroy()
		### Perform computations here ###
		to_be_written_csv={}
		self.var=StringVar()
		nr=float(computations)
		
		true=1		
		h=float(inaltime)*10
		b=float(latime)*10
		hpl=float(grosime_placa)*10
		c=25
		As_prim=float(arie)
		a_prim=float(phi)/2+c
		
		fcd=(beton.fck)/1.5
		fyd=(otel.fyk)/1.15
		d=h-(c+10)
		ds=d-a_prim
		print (c,beton.fctm)
		M=float(mom)*10**6
		
		if 2*(M-As_prim*fyd*ds)/(b*fcd)>d**2:
			messagebox.showerror("Eroare","Moment prea mare pentru seciunea data \nx negativ 2*(M-As_prim*fyd*ds)/(b*fcd)>d**2 \nSchimbati sectiunea")
			true=0

		x=d-sqrt(d**2-((2*(M-As_prim*fyd*ds)/(b*fcd))))
		Rho_min=max((float(0.5)*beton.fctm)/otel.fyk,1.13/1000)

		if x>0.25*d:
			messagebox.showerror("Eroare","x mai mare ca xlim")
			true=0
		else:
			if x<2*a_prim:
				x=2*a_prim
				As=M/(fyd*ds)
			else :
				As=b*x*fcd/fyd+As_prim

			Rho=As/(b*d)	
			
				
		
		
		if Rho>Rho_min:
			all_solutions = proper_closest(As,nr)
			not_minimum=0
		else:
			As_min=Rho_min*b*d
			minimum_solutions=proper_closest(As_min,nr)
			messagebox.showinfo("Titlu","Armare la  procent minim \nArie minima: " + str (round(As_min,2))+"\nProcent minim: "+str (round(Rho_min*1000,3)))
			not_minimum=1


		

		# n_solutions to be implemented by user/if none - by default
		all_solutions = proper_closest(As,nr) 	
	
		#defines position of the first labels	
		poz_y=0.1
		poz_x=0.32
		
		counter=0
		v=0
		
		
		if not_minimum==0:
			for s in all_solutions:
				As_ef=s[2]
				d_ef=h-(c+s[0]/2)			
				Rho=As_ef/(b*d_ef)

			# must take maximum phi for the d_ef!!						
				d_ef=h-(c+s[0]/2)
				ds_ef=d_ef-a_prim 
				x_ef=d_ef-sqrt(d_ef**2-((2*(M-As_prim*fyd*ds_ef)/(b*fcd))))
				if x>0.25*d:
					messagebox.showerror("Eroare","x mai mare ca xlim")
					true=0
				else:
					if x_ef<2*a_prim:
						x_ef=2*a_prim
						M_cap=(As_ef*fyd*ds_ef)/(10**6)#kNm
					else :
						M_cap=(As_prim*fyd*ds_ef+b*x_ef*fcd*(d_ef-x_ef/2))/(10**6)#kNm

					Rho=As_ef/(b*d_ef)
			
				
			
				
				if true==1:
					
					
					
				
				#Mcap
					label = Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=0.02,relx=poz_x)
					label.config(text="M cap \n[kNm]")
					self.label_display.append(label)
					
					

					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=poz_y,relx=poz_x)
					label.config(text="" + str (round(M_cap,2)))
					self.label_display.append(label)	
				#area
					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=0.02,relx=poz_x+0.1)
					label.config(text="Arie \nmm2") 
					self.label_display.append(label)
					
					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=poz_y,relx=poz_x+0.1)
					label.config(text="" + str (round(As_ef,2)))		
					self.label_display.append(label)
						
				# n phi
					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=poz_y,relx=poz_x+0.2)
					label.config(text="" + str (s[1])) 
					self.label_display.append(label)
					
				# "phi" 
					
					label=Label(self.frame,font=("Helvetica",10))
					label.pack()
					label.place(rely=poz_y,relx=poz_x+0.23)
					label.config(text="ɸ " + str (round(s[0]))+ "/m") 
					self.label_display.append(label)
	
				# procent	
					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=0.02,relx=poz_x+0.35)
					label.config(text="Procent\nArmare" ) 
					self.label_display.append(label)

				#rho 
					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=poz_y,relx=poz_x+0.35)
					label.config(text="" + str (round(Rho*1000,3)) + " ‰") 
					self.label_display.append(label)
				
				#radio button		
					radio=Radiobutton(self.frame,text="Optiunea " + str(counter+1),variable=self.var,value=v,command=self.selected)
					radio.pack(anchor=W)
					radio.place(rely=poz_y,relx=poz_x+0.47)
					self.radio_button.append(radio)
					
					
					self.to_be_written_csv[v]=s[1],s[0],M_cap,Rho
					
					poz_y=poz_y+0.05
					counter=counter+1
					v=v+1

				
			# new function for minimum rho	
		else:
			for m in minimum_solutions:
				As_ef=m[2]
								
					
				
				# must take maximum phi for the d_ef!!						
				d_ef=h-(c+m[0]/2)
				ds_ef=d_ef-a_prim 
				x_ef=d_ef-sqrt(d_ef**2-((2*(M-As_prim*fyd*ds_ef)/(b*fcd))))
				if x>0.25*d:
					messagebox.showerror("Eroare","x mai mare ca xlim")
					true=0
				else:
					if x_ef<2*a_prim:
						x_ef=2*a_prim
						M_cap=(As_ef*fyd*ds_ef)/(10**6)#kNm
					else :
						M_cap=(As_prim*fyd*ds_ef+b*x_ef*fcd*(d_ef-x_ef/2))/(10**6)#kNm

					Rho=As_ef/(b*d_ef)
				if true==1:
					
					
				#Mcap
					label = Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=0.02,relx=poz_x)
					label.config(text="M cap \n[kNm]")
					self.label_display.append(label)
					
					

					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=poz_y,relx=poz_x)
					label.config(text="" + str (round(M_cap,2)))
					self.label_display.append(label)	
				#area
					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=0.02,relx=poz_x+0.1)
					label.config(text="Arie \nmm2") 
					self.label_display.append(label)
					
					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=poz_y,relx=poz_x+0.1)
					label.config(text="" + str (round(As_ef,2)))		
					self.label_display.append(label)
						
				# n phi
					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=poz_y,relx=poz_x+0.2)
					label.config(text="" + str (m[1])) 
					self.label_display.append(label)
					
				# "phi" 
					
					label=Label(self.frame,font=("Helvetica",10))
					label.pack()
					label.place(rely=poz_y,relx=poz_x+0.23)
					label.config(text="ɸ " + str (round(m[0]))+ "/m") 
					self.label_display.append(label)
	
				# procent	
					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=0.02,relx=poz_x+0.35)
					label.config(text="Procent\nArmare" ) 
					self.label_display.append(label)

				#rho 
					label=Label(self.frame,font=("Helvetica", 10))
					label.pack()
					label.place(rely=poz_y,relx=poz_x+0.35)
					label.config(text="" + str (round(Rho*1000,3)) + " ‰") 
					self.label_display.append(label)
				
				#radio button		
					radio=Radiobutton(self.frame,text="Optiunea " + str(counter+1),variable=self.var,value=v,command=self.selected)
					radio.pack(anchor=W)
					radio.place(rely=poz_y,relx=poz_x+0.47)
					self.radio_button.append(radio)
					
					
					self.to_be_written_csv[v]=m[1],m[0],M_cap,Rho
					
					poz_y=poz_y+0.05
					counter=counter+1
					v=v+1   
		
		
		
