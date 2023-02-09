
#1. print number of earthquakes

import json

infile = open("eq_data.json", "r")

earthquakes = json.load(infile)

print(len(earthquakes["features"]))


#2. extract the location, magnitude, longitude and latitude of the location and put it in a new dictionary, name it 'eq_dict'.
# Only magnitude > 6

eq_dict = {}

for a,b in enumerate(earthquakes["features"]):
    if b["properties"]["mag"] > 6:
        eq_dict[a] = {
            "Place": b["properties"]["place"],
            "Magnitude": b["properties"]["mag"],
            "Longitude": b["geometry"]["coordinates"][0],
            "Latitude": b["geometry"]["coordinates"][1]
        }


#using the eq_dict dictionary, print out the information as shown below

print(eq_dict)