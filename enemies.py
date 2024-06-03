from powers import *
from characters import *
import time
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
        print("> We'll take it easy you right now. You have encountered Darcy, one of the infamous trix sisters.")
        time.sleep(3)
        print("> She uses her power, Darkness, against you. YOU JUST LOST 100 HEALTH POINTS! GET WRECKED.")
        time.sleep(3)
        print("> Your health is at 400. Now it's time for you to fire back.")

    def two():
        time.sleep(3)
        print("> Good job! Let's continue on out journey. This is round two...OH NO!!! ITS THE FRIGHTENING STORMY ;-;.")
        time.sleep(3)
        print("She used her power, Hurricane Sandy, against you. YOU LOST 100 HEALTH POINTS!")
        time.sleep(3)
        print("> Your health is at 300. What are you gonna do about it?")

    def three():
        time.sleep(3)
        y = input("> Congrats on getting this far! TIME FOR BOSS LEVEL, HERE COMES ICY. Fire first by inputing fire: ").lower()
        if y == ("fire"):
            print(f"{500 - user.damage} is icy's health. She fired back at you but she missed! Lucky you...:/ I guess it's your turn again.@#%$#!@")
            time.sleep(1)
        w = input("> Input attack to fire: ").lower()
        if w == ("attack"):
            print("> NO FLIPPING WAY, YOU WON SOMEHOW. Your attack blinded icy and gave her ptsd. dont ask questions :)")
