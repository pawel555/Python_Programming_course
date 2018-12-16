from math import pi as pi


class Cylinder(object):

    def __init__(self, height=1, radius=1):
        self.radius = radius
        self.height = height

    def volume(self):
        return round((pi * self.radius ** 2) * self.height, 2)

    def surface_area(self):
        return round((2 * pi * self.radius ** 2) + (2 * pi * self.radius * self.height), 2)


c = Cylinder(2, 3)

print(c.volume())

print(c.surface_area())
