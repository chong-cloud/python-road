import itertools
# 无限迭代器
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# 重复循环A,B,C
# cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
# for c in cs:
#     print(c)

# 重复显示A，3次
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

# 通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AaaBBBCCAAA'):
    print(key, list(group))

# 本质是函数的返回值相同则认为是重复元素
print("忽略大小写：")
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
