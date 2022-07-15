from functools import reduce

list_data = [1,2,3,4,5,6,7,8,9,10]
dict_data = {
    'name': 'John',
    'age': '30',
    'city': 'New York'
}


# lambda function - anonymous function
def multiply(x):
    return x * x

def multiply_for_reduce_func(x, y):
    return x * y

# Eg: to multiply all the elements in the list

# map (function, iterable)
# function will take one argument and return one argument
multiply_map_result = map(multiply, list_data)
print(f"map() without using lambda function: {list(multiply_map_result)}")
# or
multiply_map_result = map(lambda x: x*x, list_data)
print(f"map() using lambda function: {list(multiply_map_result)}")



# filter (function, iterable)
# function will take one argument and return one argument
multiply_filter_result = filter(multiply, list_data)
print(f"filter() without using lambda function: {list(multiply_filter_result)}")

multiply_filter_result = filter(lambda x: x*x, list_data)
print(f"filter() using lambda function: {list(multiply_filter_result)}")


# reduce (function, iterable)
# but the function should take two arguments
multiply_reduce_result = reduce(multiply_for_reduce_func, list_data)
print(f"reduce() without using lambda function: {multiply_reduce_result}")

multiply_reduce_result = reduce(lambda x, y: x*y, list_data)
print(f"reduce() using lambda function: {multiply_reduce_result}")

