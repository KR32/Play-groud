
# without argument - access
def hello_func():
    pass  # none


print(hello_func())


def hello_func2():
    print('hello world')  # hello_world


hello_func2()


def hello_func3():
    return 'hello world'            #


hello_func3()


def hello_func4():
    return 'hello world'  # hello_world


print(hello_func4())


"""with argument"""


def hello_func5(greeting, default='hello'):
    return '{},{} world'.format(greeting, default)  # hello_world

print(hello_func5('hi'))


def hello_func6():
    pass
