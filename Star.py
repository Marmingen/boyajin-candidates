from Vector import Vector

class Star():
    def __init__(self, name, x, y, z, label):
        self.name = name
        self.coords = Vector(x, y, z)
        self.label = label
        
    