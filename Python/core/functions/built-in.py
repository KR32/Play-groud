def recursion(value):
    if(value>0):
        result = value+recursion(value-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Result:")
recursion(6)
