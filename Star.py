from Vector import Vector

class Star():
    def __init__(self, name, x, y, z, label):
        self.name = name
        self.coords = Vector(x, y, z)
        self.label = label
        
    def dist(self, other_star):
        new_x = self.coords.x - other_star.coords.x
        new_y = self.coords.y - other_star.coords.y
        new_z = self.coords.z - other_star.coords.z
        dist = Vector(new_x, new_y, new_z)
        return abs(dist)