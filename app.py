from characters import *
from powers import *
from enemies import *


print("> Hello. Welcome to Mr. Whalen's Adventure World. It is literally the best thing in the world. You are going to enter this weird world and fight three bratty women. Easiest game, yea...")
print("> Wait..uhh...who are you?")

#making character
user = character.create_character()
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
a = input(f'> You used {user.element['power']}! You took {user.element['damage']} off of Darcy. {300 - user.element['damage']}.Congrats, newbie. WAIT. Don\'t celebrate yet... Watch out, there\'s more coming for you. Are you sure you want to continue? Your life depends on it... (y/n): ').lower()
if a == "y":
    print("> YOU KILLED HER, like a bosssssss. Watch out, they're coming for you. Are you sure you want to move on, your life depends on it...")
elif a == "n":
    print("> HAHA you just lost ")
c = input("> Do you want to continue (y/n): ")
if c == "y":
    print("> Ok, if you say so...")
elif c == "n":
    print("> BRUHHHH, BOY BYE")
encounters.two()
b = input(f'> You used {user.element['power']}! You took {user.element['damage']} off of Stormy. {300 - user.element['damage']}. Almost there buddy boy, do you wish to continue? (y/n): ').lower()
if b == "y":
    print("> THATS WHAT IM TALKING ABOUT")
if b == "n":
    print("> Flipping flipers")
encounters.three()

#use double quotes for a,b,c