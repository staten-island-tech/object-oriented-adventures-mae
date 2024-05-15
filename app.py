print("> Hello. Welcome to Mr. Whalen's Adventure World. It is literally the best thing in the world. You are going to enter this weird world and fight three bratty women. Easiest game, yea...")
print("> Wait..uhh...who are you?")
from characters import *
from powers import *
from enemies import *
#making character
character.create_character()
q = input("> Check if the information you put in is correct. (y/n) ").lower()
if q == "y":
    print("> Alright then. Let's continue and toss you in there.")
elif q == "n":
    print("> ME? It's not my fault. I think - no, I KNOW you're the one that messed up not me. FIX IT.")
    character.create_character()

#entering world
print("> Hey. You awake? You hit your head pretty hard when I tossed you. I really don't care. Anyway...")
print("> You see that road. No? Imagine it. Uh, follow it and try to use that new power of yours.")