'''Exercise 30 - Arguments

Question:  Why do you get an error, and how would you fix it?

def foo(a=2, b):
    return a + b
'''

def foo(a, b = 2):
    return a + b

print(foo(2))
print(foo(2,4))