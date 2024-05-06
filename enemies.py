class trix():
    def __init__(info, name, power, damage):
        info.name = name 
        info.power = power
        info.damage = damage 
darcy=trix("Darcy","Darkness",100)
stormy=trix("Stormy","Hurricane Sandy",100)
icy=trix("Icy","Flurry Fury",100)

def attack(self,trix):
    x = self.health-trix.damage
    return x 


def encounter_one():
    print("You have encountered Darcy, one of the infamous trix sisters. She uses her power, Darkness, against you. YOU JUST LOST 100 HEALTH POINTS! GET WRECKED.")
    print("Your helath is at 400")
    
encounter_one()