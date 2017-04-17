# Values are saved to csv as text. Reconvert manually if needed
import csv
def dictionary_to_csv(dictionary,keys,csv_filename):
	
	f = open(csv_filename,"w")

	row_of_keys = ""
	for k in keys:
		row_of_keys = row_of_keys + "," + str(k)
	print(row_of_keys.strip(","),file=f)


	for i in range(len(dictionary["ρ [‰]"])):
		row_of_values = ""
		for k in keys:
			row_of_values = row_of_values + "," + str(dictionary[k][i])	
			
			
		print(row_of_values.strip(", "),file=f)	

	f.close()
