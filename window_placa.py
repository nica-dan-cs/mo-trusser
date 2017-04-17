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

class window_placa(window):

	### Define class wide variables here for anything that must be seen across multiple functions ###
	tb_grosime = None
	tb_mom = None
	tb_acoperire = None
	tb_computations=None
	tb_name=None
	tb_location=None
	
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
		
		#Grosime	
		label = Label(self.frame,text="Grosime                   cm",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.05)
		self.tb_grosime = Text(self.frame,height=1,width=20)
		self.tb_grosime.pack()
		self.tb_grosime.place(rely=0.08)
		

		#Mom
		label = Label(self.frame,text="Moment                  kNm",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.12)
		self.tb_mom = Text(self.frame,height=1,width=20)
		self.tb_mom.pack()
		self.tb_mom.place(rely=0.15)

		#Acoperire
		label = Label(self.frame,text="Acoperire                  cm",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.19)
		self.tb_acoperire = Text(self.frame,height=1,width=20)
		self.tb_acoperire.pack()
		self.tb_acoperire.place(rely=0.22)
		self.tb_acoperire.insert(END,"1.5")
		
	
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
		
		#Number of computations
		label = Label(self.frame,text="Numar de combinatii",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.55)
		self.tb_computations = Text(self.frame,height=1,width=20)
		self.tb_computations.pack()
		self.tb_computations.place(rely=0.58)
		self.tb_computations.insert(END,"7")
		
		#Name
		label = Label(self.frame,text="Directie",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.62)
		self.tb_name = Entry(self.frame,width=20)
		self.tb_name.pack()
		self.tb_name.place(rely=0.65)
		

		#Location
		label = Label(self.frame,text="Pozitie",font=("Helvetica", 10))
		label.pack()
		label.place(rely=0.69)
		self.tb_location = Entry(self.frame,width=20)
		self.tb_location.pack()
		self.tb_location.place(rely=0.72)
		

		#Run Button
		run_button = Button(self.frame,text="Process",command=self.run_button_callback)
		run_button.pack()
		run_button.place(rely=0.76,relx=0.06)
		
		#Add to file  Button
		add_to_file_button = Button(self.frame,text="Add to file",command=self.add_to_file_button_callback)
		add_to_file_button.pack()
		add_to_file_button.place(rely=0.83,relx=0.06)
		
		#Create file Button
		create_file_button = Button(self.frame,text="Create File",command=self.create_file_callback)
		create_file_button.pack()
		create_file_button.place(rely=0.9,relx=0.06)
		
	
		
		
	
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
			grosime = float(self.tb_grosime.get("1.0",END))
			mom = float(self.tb_mom.get("1.0",END))
		except:
			messagebox.showerror("Invalid input","    ERROR     ")
			return
		
		acoperire = None
		try:
			acoperire = float(self.tb_acoperire.get("1.0",END))
			
		except:
			acoperire = float(1.5)
		computations=None	
		try:
			computations=float(self.tb_computations.get("1.0",END))
		except:
			computations=float(7)
		

		output = self.process(beton_ales,otel_ales,grosime,mom,acoperire,computations)
	
		### Render output to user ###

		#creates the file with all requested data
	def create_file_callback(self):
		return dictionary_to_csv(self.all_written,self.all_written_keys,"testest.csv")

	def add_to_file_button_callback(self):
		name=[]
		location=[]
		name.append(self.tb_name.get())
		location.append(self.tb_location.get())
		if name==['']:
			name=["none"]
		if location==['']:
			location=["none"]
		output=self.add_to_file(name,location) #variables defined here --> made them available in add_to_file function
		

		#function for radio button - #gets the variable from radio button - and returns its value
	def selected (self):
		self.var_selected=self.var.get()
	
		#append to all_written every chosen option along all processes made	
	def add_to_file(self,name,location):
		ceva=[]
		try:
			for h in self.to_be_written_csv:
				if float(h)==float(self.var_selected):
					for smth in self.to_be_written_csv[h]:
						ceva.append(smth)
		except:
			messagebox.showerror("Eroare","cevadfasdfsadf")
		self.all_written["Directie"].append(str(name).strip("['']")) 
		self.all_written["Pozitie"].append(str(location).strip("['']"))				
		self.all_written["Nr bare"].append(ceva[0])
		self.all_written["ɸ"].append(int(ceva[1]))
		self.all_written["Mcap [kNm]"].append(round(ceva[2],2))
		self.all_written["ρ [‰]"].append(round(ceva[3]*1000,3))
		
		

	def process(self,beton,otel,grosime,mom,acoperire,computations):
		
		### Perform computations here ###
		to_be_written_csv={}
		self.var=StringVar()


		true=1		
		h=float(grosime)*10
		
		b=1000
		fcd=(beton.fck)/1.5
		fyd=(otel.fyk)/1.15
		c=float(acoperire)*10
		d=h-(c+5)
		M=float(mom)*10**6
		if (2*M)/(b*fcd)>d**2:
			messagebox.showerror("Eroare","Moment prea mare pentru seciunea data \nx negativ \nSchimbati sectiunea")
			true=0
		
		x=d-sqrt(d**2-(2*M)/(b*fcd))
		
		if otel.comercial_name=="OB 37":
			x_lim=0.6*d
		elif otel.comercial_name=="PC 52" or otel.comercial_name=="PC 60":
			x_lim=0.55*d
		elif otel.comercial_name=="BST 500":
			x_lim=0.467*d

		if x>x_lim:
			messagebox.showinfo("Atentie","X mai mare ca x lim \nSchimbati sectiunea")
			true=0
		else:
			As=(b*x*fcd)/fyd
		Rho_min=max((0.26*beton.fctm)/otel.fyk,1.13/1000)
		
		nr=float(computations)

		# n_solutions to be implemented by user/if none - by default
		all_solutions = proper_closest(As,nr) 	
		
		#defines position of the first labels	
		poz_y=0.1
		poz_x=0.32
		
		counter=0
		v=0
		
	#clears the labels
		for l in self.label_display:
			l.place_forget()
		
 	#destroys radio buttons
		for l in self.radio_button:
			l.destroy()
	
		for s in all_solutions:
			As_ef=s[2]
			d_ef=h-(c+s[0]/2)			
			Rho=As_ef/(b*d_ef)		
			if Rho<Rho_min:
				Rho=Rho_min
				As_min=Rho*b*d
				messagebox.showinfo("Titlu","Armare la  procent minim \nArie minima: " + str (round(As_min,2))+"\nProcent minim: "+str (round(Rho_min*1000,3)))
				#takes the minimum area and finds new solutions
				minimum_solutions=proper_closest(As_min,nr)
				not_minimum=1				
				break				
				#if rho<rho_min - breaks for function all_solutions and finds new areas for as_min
				
			
			else:
				not_minimum=0				
				d_ef=h-(c+s[0]/2)
				x_ef=(As_ef*fyd)/(b*fcd)
				M_cap=(As_ef*fyd*(d_ef-x_ef/2))/(10**6) #kNm
				
				
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
		if not_minimum==1:
			for m in minimum_solutions:
				As_ef=m[2]
				d_ef=h-(c+m[0]/2)			
				Rho=As_ef/(b*d_ef)
				
				x_ef=(As_ef*fyd)/(b*fcd)
				M_cap=(As_ef*fyd*(d_ef-x_ef/2))/(10**6) #kNm
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
					

		
		
		
		
