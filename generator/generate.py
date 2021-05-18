def fib(max):
    n, a, b = 0, 2, 3
    while n < max:
        # 使用send时，用下面两行代码
        kk = yield b
        print("kk  ", kk)
        # 使用next时，用下面一行代码
        # yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 下面这行代码不会进入fib函数，因为生成器未激活，需要next或者send激活
g = fib(6)
while True:
    try:
        # x = next(g)
        # send(None)==next(),但是第一次调用时send()不能带参数，只能send(None)，因为此时没有生成器
        x = g.send(None)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 以下也叫“协程”。由一个线程执行，produce和consumer协作完成任务，所以称为“协程
def consumer():
    r = 'here'
    while True:
        n1 = yield r  # 每次yield的时候，并未赋值给n1，当produce中执行send时，发送过来的值由n1接收
        if not n1:
            return
        print('[CONSUMER] Consuming %s...' % n1)
        r = '200 OK'+str(n1)


def produce(c):
    aa = c.send(None)
    print("aa  ", aa)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r1 = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r1)
    c.close()

c = consumer()
produce(c)

# yield与yield from 对比
def fib():
    a = ("aa", "bb", )
    while True:
        yield from a
        yield a


c = fib()
for k in range(6):
    print(next(c))
