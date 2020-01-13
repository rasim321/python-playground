import csv
import json

# Read csv
with open('vegetables.csv', 'r') as f:
	vege = csv.DictReader(f)
	vegetables = list(vege)
	vegetables = [dict(row) for row in vegetables]
#Print variable: vegetables
print(vegetables)

#Write json file
with open('vegetables.json', 'w') as f:
	json.dump(vegetables,f)

#worked with inayat and mia