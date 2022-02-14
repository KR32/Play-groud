Integers = {1,2,3,4,5,66,6}

print('Integers= ',Integers)

# REMOVE
Integers.discard(66)
print('Integers= ',Integers)
print('')

# UNION (adding something....)
print("UNION")
print('')
print('     Integers= ',Integers)
real={6,7,8,9}
print('     real= ',real)
print('')
print('Integers|real  = ',Integers|real,": Union symbol ( '|' )")
print('')

# INTERSECTION (common elements....)
print("INTERSECTION")
print('')
print('     Integers= ',Integers)
real={6,7,8,9}
print('     real= ',real)
print('')
print('Integers&real  = ',Integers&real,": INTERSECTION symbol ( '&' )")
print('')

# INTERSECTION (common elements....)
print("INTERSECTION")
print('')
print('     Integers= ',Integers)
real={6,7,8,9}
print('     real= ',real)
print('')
print('Integers&real  = ',Integers&real,": INTERSECTION symbol ( '&' )")
print('')

# DIFFERENCE (uncommon elements of first set by removing commen element {6}....)
print("DIFFERENCE")
print('')
print('     Integers= ',Integers)
real={6,7,8,9}
print('     real= ',real)
print('')
print('Integers-real  = ',Integers-real,": DIFFERENCE symbol ( '-' )")
print('')

# SYMMETRIC DIFFERENCE (all the uncommon elements between two sets by removing commen element {6})
print("SYMMETRIC DIFFERENCE")
print('')
print('     Integers= ',Integers)
real={6,7,8,9}
print('     real= ',real)
print('')
print('Integers^real  = ',Integers^real,": SYMMETRIC DIFFERENCE symbol ( '^' )")
print('')
