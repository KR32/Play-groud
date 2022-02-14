# Break helps to stop the loop
# Continue helps to iterate the loop

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        #break
        #continue
    print(num)

""" 
############    while break

1
2
Found!

#############    while continue

1
2
Found!
4
5

"""
for num in nums:
    for letter in 'abc':
        print(num,letter)

"""
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
4 a
4 b
4 c
5 a
5 b
5 c

"""
for i in range(10):
    print(i)

"""
0
1
2
3
4
5
6
7
8
9
"""
for i in range(1,11):
    print(i)

"""
1
2
3
4
5
6
7
8
9
10
"""
#while loop

x=0
while x<10:
    print(x)
    x+=1
"""
0
1
2
3
4
5
6
7
8
9
"""
#infinit loop press ctrl+c to cancel the looping 
# while True:
#     if x==5:
#         break
#     print(x)
#     x+=1