import turtle

class peepaw:
    def __init__(self, image, title):
        self.image = image
        self.title = title
    def create(self):   
        screen = turtle.Screen()
        screen.register_shape("peepaw-grandpa-fairy.gif")
        screen.addshape("peepaw-grandpa-fairy.gif")
        turtle.shape("peepaw-grandpa-fairy.gif")
        turtle.mainloop()










