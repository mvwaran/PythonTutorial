# Class have PROPERTIES (self) and METHODS

class Human:

    eyes = 2

    def __init__(self, name, isMale):
        self.name = name
        self.isMale = isMale

    def think(self):
        print("Thinking")

    def walk(self):
        print("Walking")