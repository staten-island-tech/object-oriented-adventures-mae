class powers(): #template for the powers
    def __init__(info, power, damage):
        info.power = power
        info.damage = damage
#creates the different powers
nature = powers("Deforestation", 100)
fire = powers("Volcano Boom", 125)
water = powers("Hurricane-y Spin-y", 100)
light = powers("Sun Burnt Oven", 125)
music = powers("Deafening Speakers", 100)
# class User():
#     power: {}
# Agnes['power'] = water.__dict__()       WHALEN'S EXAMPLE
def choosing_power(character):
    x = ("Now that you just recieved that blow like a stupid dummy. Attack back. Which element would you like to utilize? (n/f/w/l/m): ").lower()
    if x == "n":
        character['power'] = nature.__dict__() #adds the power you choose to your dictionary as a character.
    elif x == "f":
        character['power'] = fire.__dict__()
    elif x == "w":
        character['power'] = water.__dict__()
    elif x == "l":
        character['power'] = light.__dict__()
    elif x == "m":
        character['power'] = music-__dict__()

print(f"> You used {character['power'].power}! You took {character['power'].damage} off of Icy. {500 - character['power'].damage}.Congrats, newbie. WAIT. Don't celebrate yet... Watch out, she's coming for you.") #for when you use the power against the trix
