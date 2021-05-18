# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

import functools

int8 = functools.partial(int, base=8)

# 8进制表示为16，10进制为14
print(int8("16"))