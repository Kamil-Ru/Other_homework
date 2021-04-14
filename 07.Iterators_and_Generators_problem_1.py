'''
Problem 1
Create a generator that generates the squares of numbers up to some number N.
'''


def gen_squares(n):
    for number in range(n):
        yield number**2
        
# TEST

for x in gen_squares(10):
    print(x)
