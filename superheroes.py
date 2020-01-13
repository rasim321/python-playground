import json

with open('superheroes.json.1', 'r') as f:
	superheroes = json.load(f)

#print(superheroes)

#empty array
powers =[]

members = superheroes["members"]
for i in members:
	powers.append(i["powers"])
print(powers)