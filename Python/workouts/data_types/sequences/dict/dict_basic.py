#  Dictionary name={key:value}
contessa={
    'manufacturer':'hindustan motors',
    'fuel' : 'diesal',
    'top speed' : '140kmph',
    'Production' : '1984–2002'
}
print(contessa)

# type conversion

#  convert list to dict
my_list = ["apple", "banana", "cherry"]
print(my_list,type(my_list))
my_list=enumerate(my_list)
print(dict(my_list))

# convert tuple to dict
my_list = ("apple", "banana", "cherry")
print(my_list,type(my_list))
my_list=enumerate(my_list)
print(dict(my_list))

# convert set to dict
my_list={"apple", "banana", "cherry"}
print(my_list,type(my_list))
my_list=enumerate(my_list)
print(dict(my_list))