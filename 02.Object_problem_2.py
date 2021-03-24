'''Object Oriented Programming
Problem 2
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        pass
        
    def volume(self):
        pass
    
    def surface_area(self):
        pass

# EXAMPLE OUTPUT
c = Cylinder(2,3)

c.volume()
out = 56.52

c.surface_area()
out = 94.2'''

class Cylinder:
    
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height
        
    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * (self.radius + self.height)

## Test:
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())