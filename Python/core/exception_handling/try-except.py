
# print('enter number4:')
# num=input()
# if num:
#     raise RuntimeError("i have some input from you!")

number='str'
try:
    number=number+1
except:
    print('number')


num = 6
assert num != 6, "the given number is 6"
print("the given number is not 6")


# output:
# number
# Traceback (most recent call last):
#   File "try-except.py", line 15, in <module>
#     assert num != 6, "the given number is 6"
# AssertionError: the given number is 6
