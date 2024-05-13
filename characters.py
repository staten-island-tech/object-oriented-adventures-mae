class character():
    def __init__(self, name,age, gender, element):
        self.name = name
        self.gender = gender
        self.age =age
        self.element = element

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Element: {self.element}")
    
    def create_character():
        name = input("Enter character name: ")
        age = int(input("Enter character age: "))
        gender = input("Enter characters gender: ")
        # element = input("Choose characters element (fire, water, earth, air): ")
        return character(name, age, gender)


   


        
