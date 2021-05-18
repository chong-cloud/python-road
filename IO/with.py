# 实现了上下文协议的上下文管理器就能使用with
# 实现了__enter__和__exit__这两个方法就是实现了上下文协议。
# 下面这一行代码的k是__enter__方法的返回值，__exit__的四个参数一个都不能少
from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen

with open("skyland.txt", "w+", encoding="utf-8") as k:
    k.writelines(["123", "kk", "\n"])


# 自定义的工具
class Test:
    enter = 'Enter...'
    exit = 'Exit...'

    def __enter__(self):
        print(Test.enter)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(Test.exit)


with Test() as te:
    print('This is test')


# 上述类简化
class Test:
    def __init__(self):
        self.enters = 'Enter...'
        self.exits = 'Exit...'

    def test(self):
        print(self.enters, self.exits, "哈哈哈")

@contextmanager
def testkk():
    print("进入生成器")  # 这部分相当于__enter__
    yield Test()
    print("我走了，再见")  # 这部分相当于__exit__


with testkk() as k:
    k.test()

# closing让所有对象都能用with，避免使用try..catch...
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line.decode("utf-8"))

# # closing的本质
# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()


