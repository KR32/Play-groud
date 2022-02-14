#  1) deleting a variable
#  2) int (vs) float in division
#  3) non-trivial assignments
#  4) Using complex-numbers
#  5) assignments
#  6) multiline


#  deleting a variable
print('deleting a variable:')
x=233
print(x)
del(x)
# print(x) # can not print x
print()


# int (vs) float in division
print('int (vs) float in division:')
x = 10/3
print("10/3 ="+str(x))
x=10//3
print("10/3 ="+str(x))
print()


# non-trivial assignments
print('non-trivial assignments:')
x=y=99
print(x)
print(y)
print()
a,b=3,4
print(a)
print(b)
print()


# Using complex-numbers
print('Using complex-numbers:')
a=10-3j
b=9-1j
# complex numbers are considered as points , To print the distance between two points
print(abs(a-b))
print()


#  assignments
print('assignments')
x=41
x+=1
print('''x=41
x+=1
print(x)
'''+str(x))
print()


# multiline
print('multiline str')
str ='''
this is a 
String
multiple 
line
''' 
print(str)