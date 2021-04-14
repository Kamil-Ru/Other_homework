'''Exercise 19 - Add Dictionary Key

Question: Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.
'''

d = {"a": 1, "b": 2}
'''
Expected output: 

  {'a': 1, 'c': 3, 'b': 2} 
  '''
  
d.update({'c': 3})

print(d)


d["d"] = 4

print(d)
