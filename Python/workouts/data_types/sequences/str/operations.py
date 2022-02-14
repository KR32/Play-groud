s='hello world'
print('s= ',s)
print('length :')
print(s.__len__())
print('index of w: ',s.index('w'))
print('count of "l" in s= ',s.count('l'))
print('reverse s= ',s[::-1])
print('in upper case = ',s.upper())
print('in lower = ',s.lower())
print('repeat the string "hello " in s= ',s[0:6]*2)
print('concadinate " hi" with s=',s+' hi')
print('membership testing in str')
if 'h' in s:
    print('element in s.')
