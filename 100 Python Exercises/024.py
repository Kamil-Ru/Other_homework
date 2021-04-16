'''Exercise 24 - Iterate Dictionary

Question: Please complete the script so that it prints out the expected output.
'''
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

'''
Expected output: 

b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
# my 1 answer
for i in d:
    print(f'{i} has value {d[i]}')
    
# my 2 answer
print('b has value' + str(d['b']))
print('c has value' + str(d['c']))
print('a has value' + str(d['a']))

   
    
# Answer form Udemy:

print(d.items())
for key, value in d.items():
    print(key, 'has value', value)


