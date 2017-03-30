import pandas as pd
from otel import *

metal_csv_filename = "otel.csv"

def load_all_metals():
	all_metals = []
	metals_df = pd.read_csv(metal_csv_filename)
	for i,entry in metals_df.iterrows():
		all_metals.append(otel(metals_df.iloc[i]))
	return all_metals

def load_all_metal_names():
	all_metals = load_all_metals()
	all_metals_names = []

	for metal in all_metals:
		metal_name = str(metal.european_name) + " / " + str(metal.comercial_name)
		all_metals_names.append(metal_name)

	return all_metals_names