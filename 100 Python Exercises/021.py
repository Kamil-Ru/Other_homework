'''
Exercise 21 - Dictionary Filtering

Question: Filter the dictionary by removing all items with a value of greater than 1.
'''

d = {"a": 1, "b": 2, "c": 3}

'''
Expected output: 

{'a': 1}  
'''

#answer 1

c = {}
for x in d:
    if d[x] <= 1:
        c.update({x:d[x]})
print(c)

     
#Solution from udemy
d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)
 