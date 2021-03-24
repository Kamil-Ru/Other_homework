'''Object Oriented Programming

Problem 1

Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        pass
    
    def distance(self):
        pass
    
    def slope(self):
        pass

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()
out: 9.433981132056603

li.slope()
out: 1.6'''

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**0.5

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]) 


# TEST
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li)
print(li.distance())
print(li.slope())


# my other solution for exercise "classes"

class Line_2:
    
    def __init__(self,coor1,coor2):
        self.x1 = coor1[0]
        self.x2 = coor2[0]
        self.y1 = coor1[1]
        self.y2 = coor2[1]
    
    def distance(self):
        return ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1) 

# TEST
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line_2(coordinate1,coordinate2)
print(li)
print(li.distance())
print(li.slope())