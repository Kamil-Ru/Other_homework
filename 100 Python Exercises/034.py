'''
Exercise 34 - Local Vs. Global Variables

Question: The following script throws a NameError  in the last line saying that c  is not defined. 
Please fix the function so that there is no error and the  last line can print out the value of c  (i.e. 1 ).
'''

def foo(): 
    global c
    c = 1 
    return c 
foo() 
print(c)
'''
Expected output:
1 
'''

