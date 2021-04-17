'''
Exercise 27 - Acceleration Calculator
Question: 

Create a function that calculates acceleration given initial velocity v1, 
final velocity v2, start time t1, and end time t2. The formula for acceleration is:

a = (V2 - V1) / (t2 - t1)

To test your solution, call the function by inputting values 
0, 10, 0, 20 for v1, v2, t1, and t2, respectively, and you should get the expected output.

Expected output:

0.5
'''

def Acceleration_Calculator(V1, V2, t1, t2):
    return (V2 - V1) / (t2 - t1)

V1, V2, t1, t2 = 0, 10, 0, 20

print(Acceleration_Calculator(V1, V2, t1, t2))

    
