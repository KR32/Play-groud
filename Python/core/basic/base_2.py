#  Indexing
#  1) Indexing 
#  2) Adding '+' difference
#  3) Type Casting 
#  4) Take Input from user
#  5) Repeat the string:


# 1) Indexing 
s = 'Hello,World'
print('indexing #string')
print(s)
print('first char s[0]:',s[0])
print('last char s[-1]:',s[-1])
print('last 3 char s[-3:]:',s[-3:])
print()


print('indexing #substring')
String='This is String Data'
print('String={}'.format(String))
for i in range(len(String)):
    print('{}  {}'.format(String[i],i))
print('length ={} ,String[7:19] substring from "{}" = "{}"'.format(len(String),String,String[7:19]))
print('length ={} ,String[8:19] substring from "{}" = "{}"'.format(len(String),String,String[8:19]))
print('length ={} ,String[9:19] substring from "{}" = "{}"'.format(len(String),String,String[9:19]))
print('length ={} ,String[10:19] substring from "{}" = "{}"'.format(len(String),String,String[10:19]))
print()


# 2) Using an Overloaded Operator in python (plus'+')
#It Behaves differently with Strings

print('Different #puls "+" 0perator')
a,b=3,4
print('a,b={},{}'.format(a,b))
print('a+b= {}'.format(a+b))
print()
A,B="3","4"
print("A,B='{}','{}'".format(A,B))
print("A+B= '{}'".format(A+B))
print()


# 3) Type Casting 
# Converting Data Type or Type Casting (C++ terminology)

a=4
print('a={}   type(a) = {}'.format(a,type(a)))

print('''a = str(a) 
a={} type(a) = {}'''.format(a,type(str(a))))
print()


#  4) Take Input from user
print('Take Input From User')

name=input('What is your name?')
print('hello,'+name+'!')
print()


#  5) Repeat the string:
str = 'ABCDE'
long_str=str*(15)
print('''long_str=str*(15)
'''+long_str)
print()
