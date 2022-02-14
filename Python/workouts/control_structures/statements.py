# if
n=-1
if n<0:
    print('number is less then zero.')


number=12

if number<0:
    print('number is negative.')
else:
    print('number is positive.')

number=15
if number<0:
    print('number is negative.')
elif number%2 == 0:
    print('even number')
elif number%2 != 0:
    print('odd number')
else:
    print('number is positive')

word='if-condition passed' if 1 != 0 else 'failed'
print(word)