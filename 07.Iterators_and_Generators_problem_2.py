'''
Problem 2

Create a generator that yields "n" random numbers between a low and high number (that are inputs).
Note: Use the random library. For example:

import random

random.randint(1,10)

'''
import random

def rand_num(low,high,n):
    for _ in range(n):
        yield random.randint(low,high)
    
# TEST

for num in rand_num(1,10,12):
    print(num)