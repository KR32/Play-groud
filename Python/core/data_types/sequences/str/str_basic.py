
# printing the str data

#single line str with in single quotes
print('')
print('single-line with in single quotes')
print('')
# multi line str with in single quotes
print('')
print('''
multi-line 
with in 
single quotes''')
print('')

#singel line str with in double quotes
print('')
print("single-line with in double quotes")
print('')
# multi line str with in double quotes
print('')
print('''
multi-line 
with in 
double 
quotes''')
print('')


# we  can print '' within " " like " string 'data' for test"
print("string 'data' for test")
print()
# as like as
print('string "data" for test')
print()
# also we can do like this
print('''
i have 
printed
'hello world' and "hello!"
in my python program!
''')
print()

print("""
i have 
printed
'hello world' and "hello!"
in my python program!
""")
print()

# assigning the str data to variable
print()
str_data='string "data" in a str_data address in my memory.'
print('str_data= '+str_data)
#  add two string 
str_data2='collection of information is called data'
print('str_data2= '+str_data2)
print()
print("str_data+str_data2= "+str_data+str_data2)


# Using range with str
print()
str_='stringdataABCDEFGHI'
print(str_)
# index starts with 0 while indexing like str[10] it will print 9th char
print('str_[0] = '+str_[0])
print('str_[18] = '+str_[18])
# index starts with 1 while range 
print('str_[10:18] = '+ str_[10:18])
print('str_[10:19] = '+ str_[10:19])
# test index (gives err)
print('str_[19] = '+ str_[19])