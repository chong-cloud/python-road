# 所有的生成器都是迭代器iterator的对象
# list、tuple、dict、str不是iterable的，但不是iterator对象，不过可以使用iter()将其转为iterator
# 所有iterator都可以使用next()，即惰性的，只有调用next时才给出下一个值，for循环本质不断调用next()，所有iterable都可以被iterable

aa = ["a", 1, "测试"]
aa = iter(aa)
while True:
    try:
        print(next(aa))
    except:
        print("已经全部输出")
        break

