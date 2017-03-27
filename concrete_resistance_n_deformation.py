import pandas as pd

characteristics_csv_filename = "concrete_resistance_n_deformation.csv"
characteristics_df = pd.read_csv(characteristics_csv_filename)
characteristics = {}

required_characteristics = []
for i,entry in characteristics_df.iterrows():
	required_characteristics.append(entry['Characteristic'])

required_classes = []
for required_class in characteristics_df:
	if required_class == "Characteristic":
		continue
	required_classes.append(required_class)

for i,required_characteristic in zip(range(len(required_characteristics)),required_characteristics):
	characteristics[required_characteristic] = {}
	for required_class in required_classes:
		to_be_added = characteristics_df[required_class].loc[i]
		characteristics[required_characteristic][required_class] = to_be_added

def fck(C):
	return C.strip('C').split('/')[0]

def fck_cube(C):
	return C.strip('C').split('/')[1]

def characteristic(characteristic_name,class_name):
	return characteristics[characteristic_name][class_name]