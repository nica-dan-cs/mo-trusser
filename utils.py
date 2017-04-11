# Values are saved to csv as text. Reconvert manually if needed

def dictionary_to_csv(dictionary,csv_filename):
	f = open(csv_filename,"w")
	for k in dictionary.keys():
		print(str(k) + "<--->" + str(dictionary[k]),file=f)
	f.close()

def csv_to_dictionary(csv_filename):
	f = open(csv_filename,"r")

	dictionary = {}
	for l in f:
		dictionary[l.split('<--->')[0]] = l.split('<--->')[1]

	f.close
	return dictionary