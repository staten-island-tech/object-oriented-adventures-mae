# title: mr whalen's adventure world; planning stage

# characters: self
### people make their own characters: ask for name, and gneder added to their own dictionary. create own dictionary for powers 
## character
``` python
class character(self, name, gender, element):
    self.name = name
    self.gender = gender
    self.element = {} #for varying choice of power
```

## powers
- decided powers: fire, water, nature, light, music
- class template for the elements
make a statement for when the certain power is used:
``` python
class powers(info, power, damage):
    info.power = power
    info.damage = damage
```
- line ex. template:
``` python
print(f"> You used {character['power'].power}! You took {character['power'].damage} off of Icy. {300 - character['power'].damage}.Congrats, newbie. WAIT. Don't celebrate yet... Watch out, she's coming for you.") #for when you use the power against the trix
```

## enemies
the trix: darcy, icy, stormy
- make each trix and power and include the damage they do
example: template
``` python
class trix():
    def __init__(info, name, power, damage):
        info.name = name
        info.power = power
        info.damage = damage
# example of template used:
darcy = trix("Darcy", "Darkness", 100)
```
- make lines that narrate the characters current hp and the trix.
example:
``` python
print("You have encountered Darcy, one of the infamous trix sisters. She uses her power, Darkness, against you. YOU JUST LOST 100 HEALTH POINTS! GET WRECKED.")
```


object-oriented-adventures-mae created by GitHub Classroom

