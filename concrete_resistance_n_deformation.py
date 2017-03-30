import pandas as pd

characteristics_csv_filename = "concrete_resistance_n_deformation.csv"
characteristics = {}
all_concrete_names = []

def init_concrete_resistance_n_deformation():
	characteristics_df = pd.read_csv(characteristics_csv_filename)

	required_characteristics = []
	for i,entry in characteristics_df.iterrows():
		required_characteristics.append(entry['Characteristic'])

	for concrete_name in characteristics_df:
		if concrete_name == "Characteristic":
			continue
		all_concrete_names.append(concrete_name)

	for i,required_characteristic in zip(range(len(required_characteristics)),required_characteristics):
		characteristics[required_characteristic] = {}
		for concrete_name in all_concrete_names:
			to_be_added = characteristics_df[concrete_name].loc[i]
			characteristics[required_characteristic][concrete_name] = to_be_added

def characteristic(characteristic_name,class_name):
	return characteristics[characteristic_name][class_name]