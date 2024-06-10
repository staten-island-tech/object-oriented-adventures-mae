import turtle

class peepaw:
    def __init__(self, image, title):
        self.image = image
        self.title = title
    def create(self):   
        screen = turtle.Screen()
        screen.register_shape(self.image)
        screen.addshape("peepaw-grandpa-fairy.gif")
        turtle.shape("peepaw-grandpa-fairy.gif")
        turtle.mainloop()
class trix:
    def __init__(self, image, title):
        self.image = image
        self.title = title
    def create(self):   
        screen = turtle.Screen()
        screen.register_shape("trix.gif")
        screen.addshape("trix.gif")
        turtle.shape("trix.gif")
        turtle.mainloop()
class icy:
    def __init__(self, image, title):
        self.image = image
        self.title = title
    def create(self):   
        screen = turtle.Screen()
        screen.register_shape("icy.webp")
        screen.addshape("icy.webp")
        turtle.shape("icy.webp")
        turtle.mainloop()
class stormy:
    def __init__(self, image, title):
        self.image = image
        self.title = title
    def create(self):   
        screen = turtle.Screen()
        screen.register_shape("gloomix-stormy.gif")
        screen.addshape("gloomix-stormy.gif")
        turtle.shape("gloomix-stormy.gif")
        turtle.mainloop()
class darcy:
    def __init__(self, image, title):
        self.image = image
        self.title = title
    def create(self):   
        screen = turtle.Screen()
        screen.register_shape("darcy.gif")
        screen.addshape("darcy.gif")
        turtle.shape("darcy.gif")
        turtle.mainloop()







