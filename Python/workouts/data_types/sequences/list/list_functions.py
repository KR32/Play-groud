alphabets=['A','B','C','D','E']
numbers=[1,2,3,4,'Five']
symbols=['!','@','#','$','%']
print('')
print('alphabets= '+str(alphabets))
print('numbers= '+str(numbers))
print('')

#APPEND
# Insert the element to end of the list
alphabets.append('from_append')
print('alphabets.append("from_append")= '+str(alphabets))
print('')

# INSERT
#  Insert the element to specified index of the list
numbers.insert(1,'from_insert')
print('numbers.insert(1,"from_insert")= '+str(numbers))
print('')

# EXTEND
# join two lists as a single
alphabets.extend(numbers)
print('alphabets.extend(numbers) = '+str(alphabets))
print('')

# REMOVE
#  remove the element
alphabets.remove('from_append')
print('alphabets.remove("from_append")= '+str(alphabets))
print('')

# REVERSE
# reverse the list
alphabets.reverse()
print('alphabets.reverse()= '+str(alphabets))
print('')

# CONCADENATION
# join the list like extend()
alphabets+=symbols
print('alphabets+=symbols= '+str(alphabets))
print('')

# REPETITION
# repetition
symbols*=2
print('symbols*=2= '+str(symbols))
print('')
