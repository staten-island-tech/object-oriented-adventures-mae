from powers import *
from characters import *
class trix():
    def __init__(self, name, power, damage):
        self.name = name 
        self.power = power
        self.damage = damage 
darcy=trix("Darcy","Darkness",100)
stormy=trix("Stormy","Hurricane Sandy",100)
icy=trix("Icy","Flurry Fury",100)


class encounters():   
    def one():
        print("> You have encountered Darcy, one of the infamous trix sisters. She uses her power, Darkness, against you. YOU JUST LOST 100 HEALTH POINTS! GET WRECKED.")
        print("> Your health is at 400. Now it's time for you to fire back.")

    def two():
        print("> Good job! Let's continue on out journey. OH NO!!! ITS STORMY. She used her power, Hurricane Sandy, against you. YOU LOST 100 HEALTH POINTS!")
        print("> Your health is at 300. What are you gonna do about it?")

    def three():
        y = input("> Congrats on getting this far! TIME FOR BOSS LEVEL, HERE COMES ICY. Fire first by inputing fire: ").lower()
        if y == ("fire"):
            print(f"{500 - user.element['damage']} is icy\'s health. She fired back at you but she missed! Lucky you...:/ I guess it is your turn again.@#%$#!@")
        w = input("> Input attack to fire: ").lower()
        if w == ("attack"):
            print("NO FLIPPING WAY, YOU WON SOMEHOW. Your attack blinded icy and gave her ptds. dont ask questions :)")

