class powers():
    def __init__(info, power, damage):
        info.power = power
        info.damage = damage

nature = powers("Deforestation", 100)
fire = powers("Volcano Boom", 120)
water = powers("Hurricane-y Spin-y", 110)
light = powers("Sun Burnt Oven", 100)
music = powers("Deafening Speakers", 101)

def choosing_power():
    x = input("Now that you just recieved that blow like a stupid dummy. Attack back. Which element would you like to utilize? (n/f/w/l/m)").lower()
    if x 