import math


class Line(object):

    def __init__(self, coor1, coor2):
        """Initialize instance attributes with tuples (x1,y1)  and (x2,y2)
        """
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        """Calculate the length of the segment (line)
        """
        return math.sqrt((self.coor1[1] - self.coor2[1]) ** 2 + (self.coor1[0] - self.coor2[0]) ** 2)

    def slope(self):
        """ Return the slope of a line going through the ends ( the 'a' in y=ax+b)
        """
        return (self.coor1[1] - self.coor2[1]) / (self.coor1[0] - self.coor2[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())
