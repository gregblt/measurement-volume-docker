import csv
import json
lut=[]
with open('../data/lut/freesurfer-lut', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		if row[1] != "":
			print(row[0],row[1])
			lut.append({
				'label':row[0],
				'roi':row[1]
				})
		elif row[2] != "":
			print(row[0],row[2])			
			lut.append({
				'label':row[0],
				'roi':row[2]
				})
		else:
			print(row[0],row[3])	
			lut.append({
				'label':row[0],
				'roi':row[3]
				})

with open('../data/lut/freesurfer-lut-spine', 'w') as f: 
	json.dump(lut,f,indent=4, separators=(',', ': '))

