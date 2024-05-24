print("> Hello. Welcome to Mr. Whalen's Adventure World. It is literally the best thing in the world. You are going to enter this weird world and fight three bratty women. Easiest game, yea...")
print("> Wait..uhh...who are you?")
from characters import *
from powers import * 
from enemies import *
#making character
user = character.create_character()
character.create_character()
q = input("> Check if the information you above is correct. (y/n) ").lower()
if q == "y":
    print("> Alright then. Let's continue and toss you in there.")
elif q == "n":
    print("> ME? It's not my fault. I think - no, I KNOW you're the one that messed up not me. FIX IT.")
    character.create_character()


#entering world
print("> Hey. You awake? You hit your head pretty hard when I tossed you. I really don't care. Anyway...")
print("> You see that road. No? Imagine it. Uh, follow it and try to use that new power of yours.")
print("> Ever heard of the trix? Three girls, awful style - no? me neither. They really wanna kill you. Have FUN!!")
encounters.one()
<<<<<<< HEAD
a = input(f"> You used {user.element['power']}! You took {user.element['damage']} off of Darcy. {300 - user.element['damage']}.Congrats, newbie. WAIT. Don't celebrate yet... Watch out, there's more coming for you. Are you sure you want to continue? Your life depends on it... (y/n): ").lower()
=======
a = input(f"> You used {user.element['power']}! You took {user.element['damage']} off of Darcy. {300 - user.element['damage']}.Congrats, newbie. WAIT. Don\'t celebrate yet... Watch out, there\'s more coming for you. Are you sure you want to continue? Your life depends on it... (y/n): ").lower()
>>>>>>> 6d34990c595a29202a31ca065b9d089dab637895
if a == "y":
    print("> Ok, if you say so...")
elif a == "n":
    print("> BRUHHHH, BOY BYE")
encounters.two()
<<<<<<< HEAD
b = input(f"> You used {user.element['power']}! You took {user.element['damage']} off of Stormy. {300 - user.element['damage']}. Almost there buddy boy, do you wish to continue? (y/n): ").lower()
=======
b = input(f"> You used {user.element['power']}! You took {user.element['damage']} off of Stormy. {300 - user.element['damage']}. Her ego is so big she ran away crying. Almost there buddy boy, do you wish to continue? (y/n): ").lower()
>>>>>>> 6d34990c595a29202a31ca065b9d089dab637895
if b == "y":
    print("> THATS WHAT IM TALKING ABOUT")
if b == "n":
    print("> Flipping flipers")
encounters.three()
