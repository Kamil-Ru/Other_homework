'''
Exercise 32 - Global Variables

Question:  What will the following script output? Please try to do this by mind if you can.
'''

c = 1
def foo():
    return c
c = 3
# 3
print(foo())


