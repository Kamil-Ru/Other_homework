''' 
Problem 2
Handle the exception thrown by the code below by using 'try' and 'except' blocks. Then use a finally block to print 'All Done.'
'''



try:
    x = 5
    y = 0
    z = x/y
except:
    print('ZeroDivisionError: division by zero')
finally:
    print('All Done.')


