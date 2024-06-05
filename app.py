from characters import *
from powers import *
from enemies import *
<<<<<<< HEAD
import time
print("> Hello. Welcome to Mr. Whalen's Adventure World.")
time.sleep(2)
print("> It is literally the best thing in the world. You are going to enter this weird world and fight three bratty women. Easiest, quickest game, yea...")
time.sleep(1)
print("> Im Mr. Baldie: Mr Whalen's Butler. Wait..uhh...who are you?")
time.sleep(1)
#making character-------------------------------------------------------------
user = character()
q = input("> Check if the information you above is correct. (y/n): ").lower()
=======
#making character
user = character.create_character()
q = input("> Check if the information you above is correct. (y/n) ").lower()
>>>>>>> bf226cd90767be59b1ab19ae1d5d0bc683ad6c7b
if q == "y":
    print("> Alright then. Let's continue and toss you in there.")
elif q == "n":
    print("> ME? It's not my fault. I think - no, I KNOW you're the one that messed up not me. FIX IT.")
    character.create_character()
else:
    print("- So... is it right or wrong? Did the outside world degrade so much that you don't even know how to read?")
    time.sleep(3)
    q = input("> it's alright. you'll learn during your brief trip here. For now, is the information above right? (y/n): ").lower()
    
#entering world-------------------------------------------------------------
print("> Hey. You awake? You hit your head pretty hard when I tossed you. I really don't care. Anyway...")
print("> You see that road. No? Imagine it. Uh, follow it and try to use that new power of yours.")
print("> Ever heard of the trix? Three girls, awful style - no? me neither. They really wanna kill you. Have FUN!!")
<<<<<<< HEAD
time.sleep(3)
#-------------------------------------------------------------
encounters.one()
print(f"> You used {user.element['power']}! You took {user.element['damage']} off of Darcy. She went poof but dont worry she was the weakest and easiest one. congrats, newbie.")
time.sleep(1)
a = input(f"> WAIT. Don't celebrate yet... Watch out, there's more coming for you. Are you sure you want to continue? Your life depends on it... (y/n): ").lower()
=======
encounters.one()
<<<<<<< HEAD
a = input(f"> You used {user.element['power']}! You took {user.element['damage']} off of Darcy. {300 - user.element['damage']}.Congrats, newbie. WAIT. Don\'t celebrate yet... Watch out, there\'s more coming for you. Are you sure you want to continue? Your life depends on it... (y/n): ").lower()
=======
a = input(f"> You used {user["element"].power}! You took {user["element"].damage} off of Darcy. {300 - user["element"].damage}.Congrats, newbie. WAIT. Don't celebrate yet... Watch out, there's more coming for you. Are you sure you want to continue? Your life depends on it... (y/n): ").lower()
>>>>>>> 41584907c2d881461a8efe62f1af1fd4c7bc4cbe
>>>>>>> bf226cd90767be59b1ab19ae1d5d0bc683ad6c7b
if a == "y":
    print("> Ok, if you say so...")
elif a == "n":
    print("> BRUHHHH, BOY BYE")
else:
    print("- here we go again. just read it says y/n pick one.")
    time.sleep(1)
    input("> Do you want to continue? (y/n): ")
#-------------------------------------------------------------
encounters.two()
<<<<<<< HEAD
print(f"> You used {user.element['power']}! You took {user.element['damage']} off of Stormy. {300 - user.element['damage']}.")
time.sleep(1)
b = input(f"> Almost there buddy boy, do you wish to continue? (y/n): ").lower()
if b == "y":
    print("> THATS WHAT IM TALKING ABOUT")
elif b == "n":
    print("> Flipping flipers")
else:
    print("- OH MY GOD. SHUT UP RIGHT NOW. JUST $%#! READ. cmon we are half way through your trip and you learned nothing.")
    time.sleep(1)
    input("> do you wish to continue? (y/n): ")
#-------------------------------------------------------------
encounters.three()
time.sleep(1)
print("> Okay. Now that you miraculously beat the %#$! out of Icy. You're kinda done.") 
time.sleep(1)
w = input("> I'm assuming you wanna go back home, right? (y/n): ").lower()
if w == "y":
    print("> yea, you know what, we didn't want you here anyway. go away.")
elif w == "n":
    print("> hah...we would absolutely lovee to keep you here, but uh yea we don't like you. we don't want you here. go away.")
else:
    print("- that wasn't an option...HAVE YOU LEARNED NOTHING? read, please.")
    w = input("> Do you or do you not want to go home? (y/n): ").lower()
=======
<<<<<<< HEAD
b = input(f"> You used {user.element['power']}! You took {user.element['damage']} off of Stormy. {300 - user.element['damage']}. Her ego is so big she ran away crying. Almost there buddy boy, do you wish to continue? (y/n): ").lower()
=======
b = input(f"> You used {user["element"].power}! You took {user["element"].damage} off of Stormy. {300 - user["element"].damage}. Almost there buddy boy, do you wish to continue? (y/n): ").lower()
>>>>>>> 41584907c2d881461a8efe62f1af1fd4c7bc4cbe
if b == "y":
    print("> THATS WHAT IM TALKING ABOUT")
if b == "n":
    print("> Flipping flippers")
encounters.three()


>>>>>>> bf226cd90767be59b1ab19ae1d5d0bc683ad6c7b
