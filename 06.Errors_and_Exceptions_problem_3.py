'''
Problem 3
Write a function that asks for an integer and prints the square of it. Use a 'while loop' with a 'try', 'except', 'else block' to account for incorrect inputs.

def ask():
    pass

ask()

out:    
Input an integer: null
An error occurred! Please try again!
Input an integer: 2
Thank you, your number squared is:  4

'''

def ask():
    while True:
        try:
            number = int(input('Please input some number: '))
            print('Input an integer: {}.'.format(number))
        except:
            print('An error occurred! Please try again!')
        else:
            break
    
    number = number**2
    print('Thank you, your number squared is: {}.'.format(number))

ask()