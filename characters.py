from powers import *
class character():
    def __init__(self):
        self.name = input("- Enter character name: ").title()
        self.age = int(input("- Enter character age: "))
        self.gender = input("- Enter characters gender (f/m): ").lower()
        self.element = choosing_power()

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Element: {self.element}")
        
        

""" 
user = character("agnes", 45,'f', {"element": "music", "power": "Deafening Speakers", "damage": 100})  """


