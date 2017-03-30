import pandas as pd
from otel import *

metal_csv_filename = "otel.csv"
all_metals = []
all_metals_names = []

def load_all_metals():
	metals_df = pd.read_csv(metal_csv_filename)
	for i,entry in metals_df.iterrows():
		all_metals.append(otel(metals_df.iloc[i]))

	for metal in all_metals:
		metal_name = str(metal.european_name) + " / " + str(metal.comercial_name)
		all_metals_names.append(metal_name)

def get_all_metals():
	return all_metals

def get_all_metals_names():
	return all_metals_names

def get_metal_by_names(names):
	european_name = names.split(" / ")[0]
	comercial_name = names.split(" / ")[1]
	for metal in all_metals:
		if( (metal.european_name == european_name) & (metal.comercial_name == comercial_name) ):
			return metal