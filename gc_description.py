#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

# 第一种，装饰器无参数
def log(func):
    # 下一行用于修改方法的名称，若没有now.__name__变为装饰器的方法名
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

# 第二种，装饰器有参数
def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)


# 理解@functools.wraps(func)
def gc(fn1):
    # @functools.wraps(fn1)
    def test_gc(*kk):
        print("运行了test_gc"+str(kk))
        fn1()
    return test_gc

@gc
def gc_kk():
   print("运行了gc_kk")

@gc
def gc_ss():
   print("运行了gc_ss")


if __name__ == "__main__":
    gc_kk("12", 15)
    print(gc_kk.__name__)
    gc_ss()
    print(gc_ss.__name__)