alpha=('a','b','c','d')
print('alpha= '+str(alpha))

print('')
print('we can not edit the data into the tuple.this is called immutable.')
print('')

# INDEXING
print('alpha[0],alpha[1]= '+str(alpha[0])+','+str(alpha[1]))
print('')

# Know the element's Index
print('alpha.index("d")=',alpha.index("d"))
print('')

# SLICING
print('alpha[0:3]= ',alpha[0:3])
print('')

print('alpha[0:4]= ',alpha[0:4])
print('')

print('alpha[0:]= ',alpha[0:])
print('')

print('alpha[:4]= ',alpha[:4])
print('')

print('alpha[:-1]= ',alpha[:-1])
print('')

print('alpha[::-1]= ',alpha[::-1])
print('')

print('alpha[-1:]= ',alpha[-1:])
print('')

print('alpha[-1::]= ',alpha[-1::])
print('')

# CONCATENATION
numeric=(1,2,3,4)
print('numeric=',numeric)
print('alpha= ',alpha)

print('alpha+numeric= ',alpha+numeric)
print('')

# REPETITION
print('alpha*2= ',alpha*2)
new=alpha*2

# COUNT REPETITION OF ELEMENT
print('new= ',new)
print('new.count("a")= ',new.count("a")) 
print('')

# GET THE TOTAL No OF ELEMENTS in TUPLE
print('numeric= ',numeric)
print('numeric.__len__() = ',numeric.__len__() )
print('') 