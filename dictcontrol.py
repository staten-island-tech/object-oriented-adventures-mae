import json
import os
## Create Class for creating new dictionaries here

class character():
    def __init__(self, name, gender, power, t): 
        self.name = name 
        self.gender = gender 
        self.power = power 
        self.type = t
    def __str__(info):
        return f"{info.name},{info.gender},{info.power},{info.t}"
class powers():
    def __init__(info, damage, name, element, t):
        info.damage = damage
        info.name = name 
        info.element = element
        info.type = t
    def __str__(info):
        return f"{info.damage},{info.name},{info.element},{info.t}"
class nature(powers):
    def __init__(info, name, damage, t):
        info.name = name 
        info.damage = damage
        info.type = t
    def __str__(info):
        return f"{info.name},{info.damage},{info.t}"
class water(powers):
    def __init__(info, name, damage, t):
        info.name = name 
        info.damage = damage
        info.type = t
    def __str__(info):
        return f"{info.name},{info.damage},{info.t}"
class fire(powers):
    def __init__(info, name, damage, t):
        info.name = name 
        info.damage = damage
        info.type = t
    def __str__(info):
        return f"{info.name},{info.damage},{info.t}"
class music(powers):
    def __init__(info, name, damage, t):
        info.name = name 
        info.damage = damage
        info.type = t
    def __str__(info):
        return f"{info.name},{info.damage},{info.t}"
class light(powers):
    def __init__(info, name, damage, t):
        info.name = name
        info.damage = damage
        info.type = t
    def __str__(info):
        return f"{info.attack},{info.damage},{info.t}"



with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here


def add_nature(species, lifespan, gender, ocean, t):
    add_marine = nature(species, lifespan, gender, ocean, t)
    data.append(add_marine.__dict__)


def add_land(species, lifespan, gender, continent, t):
    add_land = land(species, lifespan, gender, continent, t)
    data.append(add_land.__dict__)

y = ('Y')
while y == ("Y"):
    x = input("What type of mammal are you adding? (marine/land)").title()
    if x == ('Marine'):
        species = input("What is the species of the mammal?").title()
        lifespan = input("What is the lifespan of the mammal?").title()
        gender = input("What is the gender of the mammal?").title()
        ocean = input("What is the ocean the mammal is found in").title()
        t = x
        add_marine(species, lifespan, gender, ocean, t) 
    if x == ('Land'):
        species = input("What is the species of the mammal?").title()
        lifespan = input("What is the lifespan of the mammal?").title()
        gender = input("What is the gender of the mammal?").title()
        country = input("What is the continent the mammal is found in?").title()
        t = x
        add_land(species, lifespan, gender, country, t)
    y = input("Do you want to add another mammal? (Y/N)").upper()
 
    for i in data:
        print(i["species"])





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