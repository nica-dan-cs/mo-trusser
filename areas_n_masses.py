import pandas as pd
from tkinter import messagebox

areas_n_masses_filename = "areas_n_masses.csv"
areas_n_masses = {}

def init_areas_n_masses():
	areas_n_masses_df = pd.read_csv(areas_n_masses_filename)
	for i,entry in areas_n_masses_df.iterrows():
		phi = entry['phi']
		area_for_1 = entry['area']
		mass = entry['mass']
		areas_n_masses[str(float(phi))] = [float(area_for_1),float(mass)]
		
def area_by_phi(phi,n):
	area_for_1 = areas_n_masses[str(float(phi))][0]
	area_for_n = n * area_for_1
	return area_for_n

def mass_by_phi(phi):
	return areas_n_masses[str(phi)][1]

def area_n_mass_by_phi(phi,n):
	area = area_by_phi(phi,n)
	mass = mass_by_phi(phi)
	return [area,mass]

def all_areas_n_masses():
	return areas_n_masses

def proper_closest(area,n_solutions):
	best_solution = [] #[phi,n,area,error]
	

	all_phi = [float(k) for k in areas_n_masses.keys() if float(k) < 15]
	all_n = [i + 1 for i in range(3,11)]
	all_solutions = []
	
	
	best_solution = [0,0,0,99999999]	
	for p in range(len(all_phi)):
		for n in range(len(all_n)):
			this_area = area_by_phi(all_phi[p],all_n[n])
			if not this_area < area:
				this_error = area - this_area
				if(abs(this_error) < abs(best_solution[3])):
					best_solution = [all_phi[p],all_n[n],this_area,this_error]

	all_solutions.append(best_solution)

	n_solutions = n_solutions - 1
	while n_solutions > 0:
		best_solution = [0,0,0,99999999]	
		for p in range(len(all_phi)):
			for n in range(len(all_n)):
				this_area = area_by_phi(all_phi[p],all_n[n])
				if not this_area < area:
					this_error = area - this_area
					if(abs(this_error) < abs(best_solution[3])):
						maybe_best_solution = [all_phi[p],all_n[n],this_area,this_error]
						if not maybe_best_solution in all_solutions:
							best_solution = maybe_best_solution
		if(best_solution[3] > 99999998):
			
			return None
		
		all_solutions.append(best_solution)
		n_solutions = n_solutions - 1

	return all_solutions		

def n_phis_in_solution(s):
	phis = 0
	if not s[1][0] == 'none':
		phis = phis + 1
	if not s[2][0] == 'none':
		phis = phis + 1
	if not s[3][0] == 'none':
		phis = phis + 1
	return phis

def is_multi_phi_solution_ok(a,b,c):
	non_null = []
	if not a[0] == 'none':
		non_null.append(a)
	if not b[0] == 'none':
		non_null.append(b)
	if not c[0] == 'none':
		non_null.append(c)


	phis = []
	for nn in non_null:
		if not int(nn[0]) in phis:
			phis.append(int(nn[0]))

	if not len(non_null) == len(phis):
		return False

	n = 0
	for i in non_null:
		n = n + i[1]

	if n < 5 and len(non_null) == 3:
		return False

	return True

def phi_smaller_than_22(a,b,c):
	try:
		if abs(float(a[0])-float(b[0]))==2:			
			return False
		if abs(float(a[0])-float(c[0]))==2:
			return False
		if abs(float(b[0])-float(c[0]))==2:		
			return False
	except: 
		return True 

	
	
	return True


def bars_exceptions(a,b):
	#daca este o bara sa nu o afiseze
	try:
		if b[0]=='none':
			if a[1]==1 or a[1]==2:
				return False
	except:
		return True
	#daca sunt 2 bare , sa fie egale
	try:
		if a[1]+b[1]==2 :
			return False
	except:
		return True


	try:
	#bare mai mari in nr mai mic
		if a[1]+b[1]==3:
			if (a[0]<b[0]and a[1]>b[1]) or (a[0]>b[0] and a[1]<b[1]):
				return False
	except:
		return True
		

	#nr egal de bare din fiecare tip pt 4 bare
	try:		
		if a[1]+b[1]==4:
			if not a[1]==b[1]:
				return False
	except:
		return True
			
			
				
	#minim 2 bare de 1 tip pt 5 bare	
	try:		
		if a[1]+b[1]==5:
			if not a[1]==2 or b[1]==2:
				return False
	except:
		return True
		
			

	#bare mai mari in nr mai mic
	try:			
		if a[1]+b[1]==5:
			if (a[0]<b[0]and a[1]>b[1]) or (a[0]>b[0] and a[1]<b[1]):
				return False
	except:
		return True
			
			
	#minim 2 bare de 1 tip si nu bare egale ca numar pt 6 bare?
	try:		
		if a[1]+b[1]==6:
			if not a[1]==2 or b[1]==2:
				return False
	except:
		return True
			
	return True

def multi_phi_closest(area,n_solutions):
	best_solution = [] #[phi,n,area,error]

	#n_solutions = 299

	all_phi = [float(k) for k in areas_n_masses.keys() if float(k) > 14]
	all_n = [i  for i in range(1,6)]
	all_solutions = []
	
	all_configs = [] # phi, n, area
	for p in range(len(all_phi)):
		for n in range(len(all_n)):
			this_area = area_by_phi(all_phi[p],all_n[n])
			all_configs.append([all_phi[p],all_n[n],this_area])		
	all_configs.append(['none','none',0])

	# find first best solution
	best_solution = [9999999999,[0,0],[0,0],[0,0]]
	for ia in range(0,len(all_configs)):
		for ib in range(ia,len(all_configs)):
			for ic in range(ib,len(all_configs)):
				a = all_configs[ia]
				b = all_configs[ib]
				c = all_configs[ic]

				if not is_multi_phi_solution_ok(a,b,c):
					continue
				if not phi_smaller_than_22(a,b,c):
					continue
				if c[0]=='none' and c[1]=='none':  #pune toate conditiile pt 2 tipuri
						if not bars_exceptions(a,b):
							continue
				if  not c[0]=='none' : 	#fara 3 tipuri
						continue

				this_area = a[2] + b[2] + c[2]
				if not this_area < area:
					this_error = area - this_area
					if(abs(this_error) < abs(area - best_solution[0])):#???
						best_solution = [this_area,[a[0],a[1]],[b[0],b[1]],[c[0],c[1]]]		

	all_solutions.append(best_solution)

	n_solutions = n_solutions - 1
	while n_solutions > 0:
		best_solution = [9999999999,[0,0],[0,0],[0,0]]
		for ia in range(0,len(all_configs)):
			for ib in range(ia,len(all_configs)):
				for ic in range(ib,len(all_configs)):
					a = all_configs[ia]
					b = all_configs[ib]
					c = all_configs[ic]

					if not is_multi_phi_solution_ok(a,b,c):
						continue
					if not phi_smaller_than_22(a,b,c):
						continue
					if c[0]=='none' and c[1]=='none':
						if not bars_exceptions(a,b):
							continue
					if  not c[0]=='none' :
						continue
					
					this_area = a[2] + b[2] + c[2]
					if not this_area < area:
						this_error = area - this_area
						if(abs(this_error) < abs(area - best_solution[0])):#???
							maybe_best_solution = [this_area,[a[0],a[1]],[b[0],b[1]],[c[0],c[1]]]
							if not maybe_best_solution in all_solutions:
								best_solution = maybe_best_solution
			


		if(best_solution[0] > 99999998):
			
			return all_solutions
		
		all_solutions.append(best_solution)
		n_solutions = n_solutions - 1


	

	all_solutions_1 = []
	all_solutions_2 = []
	all_solutions_3 = []
	moved_solutions = []

	for s in all_solutions:
		n_phis = n_phis_in_solution(s)
		if abs(area - s[0]) < 500: #EROARE
			if n_phis == 1:
				all_solutions_1.append(s)
				moved_solutions.append(s)
			if n_phis == 2:
				all_solutions_2.append(s)
				moved_solutions.append(s)
			if n_phis == 3:
				all_solutions_3.append(s)
				moved_solutions.append(s)

	final_solutions = []
	for s in all_solutions_1:
		final_solutions.append(s)
	for s in all_solutions_2:
		final_solutions.append(s)
	for s in all_solutions_3:
		final_solutions.append(s)
	#for s in all_solutions:
		#if not s in moved_solutions:
			#final_solutions.append(s)

	
	return final_solutions

def multi_phi_closest_minimum(area,n_solutions):
	best_solution = [] #[phi,n,area,error]

	#n_solutions = 299

	all_phi = [float(k) for k in areas_n_masses.keys() if float(k) > 12]
	all_n = [i  for i in range(1,6)]
	all_solutions = []
	
	all_configs = [] # phi, n, area
	for p in range(len(all_phi)):
		for n in range(len(all_n)):
			this_area = area_by_phi(all_phi[p],all_n[n])
			all_configs.append([all_phi[p],all_n[n],this_area])		
	all_configs.append(['none','none',0])

	# find first best solution
	best_solution = [9999999999,[0,0],[0,0],[0,0]]
	for ia in range(0,len(all_configs)):
		for ib in range(ia,len(all_configs)):
			for ic in range(ib,len(all_configs)):
				a = all_configs[ia]
				b = all_configs[ib]
				c = all_configs[ic]

				if not is_multi_phi_solution_ok(a,b,c):
					continue
				if not phi_smaller_than_22(a,b,c):
					continue
				if c[0]=='none' and c[1]=='none':  #pune toate conditiile pt 2 tipuri
						if not bars_exceptions(a,b):
							continue
				if  not c[0]=='none' : 	#fara 3 tipuri
						continue

				this_area = a[2] + b[2] + c[2]
				if not this_area < area:
					this_error = area - this_area
					if(abs(this_error) < abs(area - best_solution[0])):#???
						best_solution = [this_area,[a[0],a[1]],[b[0],b[1]],[c[0],c[1]]]		

	all_solutions.append(best_solution)

	n_solutions = n_solutions - 1
	while n_solutions > 0:
		best_solution = [9999999999,[0,0],[0,0],[0,0]]
		for ia in range(0,len(all_configs)):
			for ib in range(ia,len(all_configs)):
				for ic in range(ib,len(all_configs)):
					a = all_configs[ia]
					b = all_configs[ib]
					c = all_configs[ic]

					if not is_multi_phi_solution_ok(a,b,c):
						continue
					if not phi_smaller_than_22(a,b,c):
						continue
					if c[0]=='none' and c[1]=='none':
						if not bars_exceptions(a,b):
							continue
					if  not c[0]=='none' :
						continue
					
					this_area = a[2] + b[2] + c[2]
					if not this_area < area:
						this_error = area - this_area
						if(abs(this_error) < abs(area - best_solution[0])):#???
							maybe_best_solution = [this_area,[a[0],a[1]],[b[0],b[1]],[c[0],c[1]]]
							if not maybe_best_solution in all_solutions:
								best_solution = maybe_best_solution
			


		if(best_solution[0] > 99999998):
			
			return all_solutions
		
		all_solutions.append(best_solution)
		n_solutions = n_solutions - 1


	

	all_solutions_1 = []
	all_solutions_2 = []
	all_solutions_3 = []
	moved_solutions = []

	for s in all_solutions:
		n_phis = n_phis_in_solution(s)
		if abs(area - s[0]) < 500: #EROARE
			if n_phis == 1:
				all_solutions_1.append(s)
				moved_solutions.append(s)
			if n_phis == 2:
				all_solutions_2.append(s)
				moved_solutions.append(s)
			if n_phis == 3:
				all_solutions_3.append(s)
				moved_solutions.append(s)

	final_solutions = []
	for s in all_solutions_1:
		final_solutions.append(s)
	for s in all_solutions_2:
		final_solutions.append(s)
	for s in all_solutions_3:
		final_solutions.append(s)
	#for s in all_solutions:
		#if not s in moved_solutions:
			#final_solutions.append(s)

	
	return final_solutions


