'''
Exercise 29 - Liquid Volume Calculator

Question:  Please write a function that calculates liquid volume 
in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.

Liquid Volume = ((4 * Pi * r**3) / 3) - (Pi * hc**2 * (3 * r - hc) / 3 )


You can then test your solution by passing 2 for h and you should get the expected output.

Expected output:

4071.5040790523717
'''
from math import pi

#1 Answer
def Liquid_Volume_Calculator(h, r=10):
    return (((4 * pi * r**3) / 3) - ((pi * h**2 * (3 * r - h)) / 3 ))
print(Liquid_Volume_Calculator(2,20))


#2 answer Python Classes and Objects (for practic)
class Calculator:
    
    def __init__(self, h, r =10):
        self.h = h
        self.r = r
        self.volume = (((4 * pi * self.r**3) / 3) - ((pi * self.h**2 * (3 * self.r - self.h)) / 3 ))
       
    def __str__(self):
        return f'Liquid Volume = {self.volume}'

print(Calculator(2,20))
