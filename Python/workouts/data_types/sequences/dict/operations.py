students = {'name':'dev','age':20}

# get perticular key's value
print("students['name']= ",students['name'])

# add new item 
students['gender']='male'
print("students['gender']='male'\n",students)

# remove perticular item with key
students.pop('gender')
print("students.pop('gender')\n",students)

# change the key's value
students['name']='tony'
print("students['name']='tony'\n students['name']= ",students['name'])

# clear all
students.clear()
print("students.clear()\n",students)