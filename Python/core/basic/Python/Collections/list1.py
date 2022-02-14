
"""
note that the below methods do not return the modified list,they just modify the original list
"""

list1=['a','b','c','d','e']
print(list1)
list1.append('f')
print(list1)

""" outout: list.append()
['a', 'b', 'c', 'd', 'e']
['a', 'b', 'c', 'd', 'e', 'f']
"""
list2=[1,2,4,5,6]
print(list2)
list2.insert(2,3)
print(list2)

"""
[1, 2, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
"""
print(list1)
print(list2)
list1.extend(list2)
print(list1)
print(list2)

"""
['a', 'b', 'c', 'd', 'e', 'f']
[1, 2, 3, 4, 5, 6]
['a', 'b', 'c', 'd', 'e', 'f', 1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
list 2 is merged to list one 
"""

list3=[1,2,2,3,4,'hello']
print(list3)
print('index of "hello" :',list3.index('hello'))

"""
[1, 2, 2, 3, 4, 'hello']
index of "hello" : 5
"""
list4=[1,2,3,4,5,5]
print(list4)
list4.remove(5)
print(list4)

"""
[1, 2, 3, 4, 5, 5]
[1, 2, 3, 4, 5]
"""
list5=[3,5,6,7,2,1]
print(list5)
list5.sort()
print(list5.sort())
print(list5)
"""
[3, 5, 6, 7, 2, 1]
None
[1, 2, 3, 5, 6, 7]

"""
list6=[5,4,3,2,1]
print(list6)
list6.reverse()
print(list6.reverse()) #None,here (5,4,3,2,1)
print(list6)
"""
[5, 4, 3, 2, 1]
None
[1, 2, 3, 4, 5]
"""
list7=['a','b','c','d','e']
print(list7)
list7.pop(4)
print(list7)

"""
['a', 'b', 'c', 'd', 'e']
['a', 'b', 'c', 'd']
"""
#########################################################################################################################
#list Build Up

num_list=[]

for i in range(5):
    num_list.append(i)
print(num_list)
"""
[0, 1, 2, 3, 4]
"""
#########################################################################################################################
#list Indexing and Slicing
list8=['a','b','c','d','e']
print(list8[:3])
"""
['a', 'b', 'c']
"""

print(list8[3:])
"""
['d', 'e']
"""

print(list8[1:3])
"""
['b', 'c']
"""
print(list8[-1])
"""
e
"""
print(list8[-3:-1])
"""
['c', 'd']
"""
###############################################List - google request###########################################################
import requests
resp=requests.get('http://www.gutenberg.org/cache/epub/57992/pg57992.txt')

text = resp.text

print(text[:300])

lines = text.split('\n')

print(lines[100:105])

