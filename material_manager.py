import pandas as pd
from metal import *

metal_csv_filename = "metal.csv"
concrete_csv_fillename = "concrete.csv"

def load_all_metals():
	all_metals = []
	metals_df = pd.read_csv(metal_csv_filename)
	for i,entry in metals_df.iterrows():
		all_metals.append(metals_df.iloc[i])
	return all_metals

def load_all_metals_as_strings():
	all_metals = load_all_metals()
	all_metals_as_strings = []

	for metal in all_metals:
		stringed_metal = ""
		for i in range(len(metal)):
			stringed_metal = stringed_metal + str(metal[i]) + "-"
		all_metals_as_strings.append(stringed_metal[:-1])

	return all_metals_as_strings