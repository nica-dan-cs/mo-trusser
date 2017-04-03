import pandas as pd

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
	all_n = [i + 1 for i in range(11)]
	all_solutions = []

	####abs value?
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
			print("NOt enough solutions possible")
			return None
		all_solutions.append(best_solution)
		n_solutions = n_solutions - 1

	return all_solutions		

					


		
