
# map()和reduce()
from functools import reduce
from collections.abc import Iterable
from collections.abc import Iterator


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))
# 改为lambda

print(reduce(lambda x, y: x * 10 + y, map(char2num, '13579')))
print(type('2134'))
print(isinstance('12345', Iterable))
print(isinstance('12345', Iterator))


# filter() 获取素数
def no_sushu(n):
    return lambda x: x % n > 0


def get_list():
    n = 1
    while True:
        n = n + 2
        yield n


def get_sushu():
    yield 2
    te = get_list()
    while True:
        n = next(te)
        yield n
        te = filter(no_sushu(n), te)

        
a = get_sushu()
for i in list(range(10)):
    print(next(a))


# sorted
kkk = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(kkk, key=str.lower, reverse=True))
print(kkk)