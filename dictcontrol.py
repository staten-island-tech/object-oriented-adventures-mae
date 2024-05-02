import json
import os
## Create Class for creating new dictionaries here

class character():
    def __init__(self, name, gender, power):
        self.name = name
        self.gender = gender
        self.power = power
    
class powers(): # basic overviewing class
    def __init__(info, name, damage, element):
        info.name = name
        info.damage = damage
        element = element

class nature(powers): 
    def __init__(info, name, damage, t):
        info.name = name
        info.damage = damage
        info.t = t
    def __str__(info):
        return f"{info.name},{info.damage},{info.gender},{info.color}"

class fire(powers):
    def __init__(info, name, origin, gender, color, t):
        info.name = name
        info.origin = origin
        info.gender = gender
        info.color = color
        info.t = t
    def __str__(info):
        return f"{info.name},{info.origin},{info.gender},{info.color},{info.type}"

class water(powers):
    def __init__(info, name, origin, gender, color, t):
        info.name = name
        info.origin = origin
        info.gender = gender
        info.color = color
        info.t = t
    def __str__(info):
        return f"{info.name},{info.origin},{info.gender},{info.color},{info.type}"
            
class music(powers):
    def __init__(info, name, origin, gender, color, t):
        info.name = name
        info.origin = origin
        info.gender = gender
        info.color = color
        info.t = t
    def __str__(info):
        return f"{info.name},{info.origin},{info.gender},{info.color},{info.type}"

class light(powers):
    def __init__(info, name, origin, gender, color, t):
        info.name = name
        info.origin = origin
        info.gender = gender
        info.color = color
        info.t = t
    def __str__(info):
        return f"{info.name},{info.origin},{info.gender},{info.color},{info.type}"



with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here


#functions that append new animals
class add():
    def character(name, gender, power):
        new_character = character(name, gender, power)
        data.append(new_character.__dict__)


y = input("Do you want to add an animal? Y/N: ").upper()
while y == ("Y"):
    q = input("What type of animal are you adding? (mammal/marine/reptile): ").lower()
    if q == "mammal":
        name = input("What is the name of your mammal? ").lower().title()
        origin = input("Where is your mammal originally from? ").lower().title()
        gender = input("What is the gender of your mammal? F/M: ").upper()
        color = input("What color is your mammal normally? ").lower().title()
        t = q
        add_mammal(name, origin, gender, color, t)
    elif q == "marine":
        name = input("What is the name of your marine animal? ").lower().title()
        origin = input("Where is your marine animal originally from? ").lower().title()
        gender = input("What is the gender of your marine animal? F/M: ").upper()
        color = input("What color is your marine animal normally? ").lower().title()
        t = q
        add_marine(name, origin, gender, color, t)
    elif q == "reptile":
        name = input("What is the name of your reptile? ").lower().title()
        origin = input("Where is your reptile originally from? ").lower().title()
        gender = input("What is the gender of your reptile? F/M: ").upper()
        color = input("What color is your reptile normally? ").lower().title()
        t = q
        add_reptiles(name, origin, gender, color, t)
    y = input("Do you want to add another animal? Y/N: ").upper()

for i in data:
    print(i["name"])




#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")

