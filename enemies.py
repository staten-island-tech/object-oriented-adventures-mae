class trix():
    def __init__(info, name, power, damage):
        info.name = name 
        info.power = power
        info.damage = damage 
darcy=trix("Darcy","Darkness",100)
stormy=trix("Stormy","Hurricane Sandy",100)
icy=trix("Icy","Flurry Fury",100)

def attack(user,trix):
    x = user.health-trix.damage
    return x 


def encounter_one():
    print("You have encountered Darcy, one of the infamous trix sisters. She uses her power, Darkness, against you. YOU JUST LOST 100 HEALTH POINTS! GET WRECKED.")
    print("Your health is at 400")

def encounter_two():
    print("Good job! Let's continue on out journey. OH NO!!! ITS STORMY. She used her power, Hurricane Sandy, against you. YOU LOST 100 HEALTH POINTS!")
    print("Your health is at 300")

def encounter_three():
    print("Congrats on getting this far! TIME FOR BOSS LEVEL, HERE COMES ICY. Fire first...")