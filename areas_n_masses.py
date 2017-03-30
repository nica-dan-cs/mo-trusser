import pandas as pd

areas_n_masses_filename = "areas_n_masses.csv"
areas_n_masses = {}

def init_areas_n_masses():
	areas_n_masses_df = pd.read_csv(areas_n_masses_filename)
	for i,entry in areas_n_masses_df.iterrows():
		phi = entry['phi']
		area_for_1 = entry['area']
		mass = entry['mass']
		areas_n_masses[str(phi)] = [float(area_for_1),float(mass)]

def area_by_phi(phi,n):
	area_for_1 = areas_n_masses[str(phi)][0]
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