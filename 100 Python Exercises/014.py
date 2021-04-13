'''Exercise 14 - Removing Duplicates

Question: Complete the script so that it removes duplicate items from the list a .
'''
a = ["1", 1, "1", 2]

'''
Expected output: 

  ['1', 2, 1] 
  
'''
#my answer:
print(list(set(a)))

#other answer
from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

#other myself
b = []
a = ["1", 1, "1", 2]
for i in a:
    if i not in b:
        b.append(i)
print(b)

# 2 point