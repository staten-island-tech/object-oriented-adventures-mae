print("> Hello. Welcome to Mr. Whalen's Adventure World. It is literally the best thing in the world. You are going to enter this weird world and fight three bratty women. Easiest game, yea...")
print("> Wait..uhh...who are you?")
from characters import *
character.create_character()
q = input("> Check if this information is correct. (y/n) ").lower()
if q == "y":
    print("Alright then. Let's continue and toss you in there.")
elif q == "n":
    print("Oh, you're dumb. I think you're the one that messed up not me. FIX IT.")
    character.create_character()
from powers import *
choosing_power(character)

