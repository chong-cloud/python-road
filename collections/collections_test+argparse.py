import argparse
import os
from collections import Counter
from collections import ChainMap
from collections import *

# 有名称的tuple
cricle = namedtuple("cricle", ("x", "y", "r"))
p = cricle(2, 3, 4)
print(p, p.x)

# 双向列表
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 有默认值的字典，默认值通过函数给
dd = defaultdict(lambda: "N/A")
dd['key1'] = 'abc'
print(dd.get("key1"))
print(dd.get("key2"))


# 串联一组dict，然后按先后顺序查找（先进的优先级高）

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
# vars()为获得对象的属性和属性值，返回格式为dict格式
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


# 没有任何参数时，打印出默认参数：
# python3 use_chainmap.py
# 结果：
# color=red
# user=guest

# 当传入命令行参数时，优先使用命令行参数：
# python use_chainmap.py -u bob
# 结果：
# color=red
# user=bob

# 同时传入命令行参数和环境变量，命令行参数的优先级较高：
# user=admin color=green python3 use_chainmap.py -u bob
# 结果：
# color=green
# user=bob

# counter计数器,本质是dict的拓展
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
# 结果：Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
c.update('hello')  # 也可以一次性update
print(c)
# 结果：Counter({'r': 2, 'o': 2, 'g': 2, 'm': 2, 'l': 2, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 'h': 1, 'e': 1})
