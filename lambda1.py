import os


remainder = lambda num: num % 2

print(remainder(5))


def test_func(num):
    print(num)
    return lambda x: x * num

result10 = test_func(10)
result100 = test_func(100)


print(result10(9))
print(result100(9))


result10 = lambda x: x * 10
result100 = lambda x: x * 100

print(result10(9))
print(result100(9))


numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

def myfunc(x):
    if x > 7:
        return x
    
result = list(filter(myfunc, numbers_list))
print(result)

result = list(filter(lambda num: (num>7), numbers_list))
print(result)


def addition(n):
    return n + n

numbers = [1,2,3,4]
result = list(map(addition,numbers))

print(result)

result = list(map(lambda x: x + x, numbers))
print(result)

numbers2 = [5,6,7,8]
result = list(map(lambda x,y: x+y, numbers, numbers2))
print(result)

clear = lambda: os.system('clear')
clear()

remainder = lambda num: num % 2

print(remainder(5))


def test_func(num):
    print(num)
    return lambda x: x * num

result10 = test_func(10)
result100 = test_func(100)


print(result10(9))
print(result100(9))


result10 = lambda x: x * 10
result100 = lambda x: x * 100

print(result10(9))
print(result100(9))


numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

def myfunc(x):
    if x > 7:
        return x
    
result = list(filter(myfunc, numbers_list))
print(result)

result = list(filter(lambda num: (num>7), numbers_list))
print(result)


def addition(n):
    return n + n

numbers = [1,2,3,4]
result = list(map(addition,numbers))

print(result)

result = list(map(lambda x: x + x, numbers))
print(result)

numbers2 = [5,6,7,8]
result = list(map(lambda x,y: x+y, numbers, numbers2))
print(result)