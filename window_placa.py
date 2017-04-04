from window import *
from tkinter import *
from tkinter.ttk import *
from material_manager import *
from beton import *
from areas_n_masses import *
from otel import *
from math import *
from tkinter import messagebox


class window_placa(window):

	### Define class wide variables here for anything that must be seen across multiple functions ###
	tb_grosime = None
	tb_mom = None
	tb_acoperire = None
	tb_computations=None
	
	label_beton = None
	listbox_beton = None

	label_otel = None
	listbox_otel = None
	
	label_display = []
	

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
		
		#Run Button
		run_button = Button(self.frame,text="Process",command=self.run_button_callback)
		run_button.pack()
		run_button.place(rely=0.67)
		
		#Info button
		info_button = Button(self.frame,text="Info",command=self.info_button_callback)
		info_button.pack()
		info_button.config(width=3)
		info_button.place(rely=0.21,relx=0.3)
		
	def info_button_callback(self):
		messagebox.showinfo("Info Button","If left empty , it takes by default 1.5 cm")

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
			
		try:
			computations=float(self.tb_computations.get(1.0,END))
		except:
			computations=float(7)
		

		output = self.process(beton_ales,otel_ales,grosime,mom,acoperire,computations)
		
		### Render output to user ###
	
	def process(self,beton,otel,grosime,mom,acoperire,computations):
		### Perform computations here ###
		true=1		
		h=float(grosime)*10
		b=1000
		fcd=(beton.fck)/1.5
		fyd=(otel.fyk)/1.15
		print (acoperire)		
			
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
		print (nr)
		all_solutions = proper_closest(As,nr) # n_solutions to be implemented by user/if none - by default	
		
		#defines position of the first labels	
		poz_y=0.1
		poz_x=0.4
		
		#clears the labels
		for l in self.label_display:
			l.config(text=" ")
		for s in all_solutions:
			As_ef=s[2]			
			Rho=As_ef/(b*d)	
			
				
			if Rho<Rho_min:
				Rho=Rho_min
				As_min=Rho*b*d
				messagebox.showinfo("Titlu","Armare la  procent minim \nArie minima: " + str (round(As_min,2))+"\nProcent minim: "+str (round(Rho_min*1000,3)))
				#takes the minimum area and finds new solutions
				minimum_solutions=proper_closest(As_min,nr)
				not_minimum=1				
				break				
				#if rho<rho_min - breaks for function all_solutions and find new areas for as_min
				
			
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
						
					poz_y=poz_y+0.05
					
					
		# new function for minimum rho	
		if not_minimum==1:
			for m in minimum_solutions:
				As_ef=m[2]			
				Rho=As_ef/(b*d)
				d_ef=h-(c+m[0]/2)
				x_ef=(As_ef*fyd)/(b*fcd)
				M_cap=(As_ef*fyd*(d_ef-x_ef/2))/(10**6) #kNm
				if true==1:
					for l in self.label_display:			
						del l
					
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
					poz_y=poz_y+0.05
					

		
		
		
		
