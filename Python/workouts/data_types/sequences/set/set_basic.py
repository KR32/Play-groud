# a set is an immutable ,unordered collection
# like tuples
# please refer maths sets

a=set()
print('a=set()  : ',type(a))
print('')

a={}
print('a={} : '+str(type(a)))
print('')

Integers={1,2,3,4,5,6,'seven'}
print('')

print('Integers= ',Integers)
print("it holds only unique values")
print('')

NewIntegers=[1,2,3,4,5,5,6,6,7,7,7,8,8,8,9,9]
print('NewIntegers= ',NewIntegers,"  ",type(NewIntegers))
NewIntegers=set(NewIntegers)
print('NewIntegers=set(NewIntegers)')
print('NewIntegers= ',NewIntegers,"  ",type(NewIntegers))
print("set holds only unique values")
print('')
