class powers(): #template for the powers
    def __init__(info, power, damage):
        info.power = power
        info.damage = damage
    def __str__(info):
        return f"{info.power},{info.damage}"
#creates the different powers
nature = powers("Deforestation", 100)
fire = powers("Volcano Boom", 125)
water = powers("Hurricane-y Spin-y", 100)
light = powers("Sun Burnt Oven", 125)
music = powers("Deafening Speakers", 100)
# class User():
#     power: {}
# Agnes['power'] = water.__dict__()       MR. WHALEN'S EXAMPLE
def choosing_power():
    x = input("> Which element would you like to utilize for this game? (n/f/w/l/m): ").lower()
    if x == "n":
        return nature.__dict__ #adds the power you choose to your dictionary as a character.
    elif x == "f":
        return fire.__dict__
    elif x == "w":
        return water.__dict__
    elif x == "l":
        return light.__dict__
    elif x == "m":
        return music.__dict__
    else:
        x = input("> Thats not an option. Read. Which element would you like to ultilize for this game? (n/f/w/l/m): ").lower()
        
#print(f"> You used {character['power'].power}! You took {character['power'].damage} off of Icy. {300 - character['power'].damage}.Congrats, newbie. WAIT. Don't celebrate yet... Watch out, she's coming for you.") #for when you use the power against the trix
