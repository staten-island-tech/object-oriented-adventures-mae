class character():
    def __init__(self, name, gender, element):
        self.name = name
        self.gender = gender
        self.element = {}

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Element: {self.element}")
        
    def create_character():
        name = input("Enter character name: ")
        age = int(input("Enter character age: "))
        gender = input("Enter characters gender: ")
        element = input("Choose characters element (fire, water, earth, air): ")
        return Character(name, age, gender, element)

    def main():
        print("Welcome to Character Creation!")
        character = create_character()
        character.display_info()

    create_chracater().display_info(

        
