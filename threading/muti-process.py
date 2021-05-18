from multiprocessing import Process, Pool
import multiprocessing
import random
import time
import os
n = 0
"""
在Unix/Linux下，可以使用fork()调用实现多进程。
要实现跨平台的多进程，可以使用multiprocessing模块。
进程间通信是通过Queue、Pipes等实现的。
"""


# 当多个进程共享一个全局变量时，会各自创建该变量的副本，互不影响
# def task1(name):
#     global n
#     while True:
#         n += 1
#         time.sleep(1)
#         print(os.getppid(), os.getpid(), name, n)
#
#
# def task2(name):
#     global n
#     while True:
#         n += 1
#         time.sleep(2)
#         print(os.getppid(), os.getpid(), name, n)

# # 自定义进程
# # 重写run方法，如果传入参数则还需重写init方法
#
# class MyProcess(Process):
#     def __init__(self, name):
#         # 重写init方法
#         super(MyProcess, self).__init__()
#         self.name = name
#     # 因为运行start()方法后最后会执行run(),所有自定义部分放在run()方法中
#
#     def run(self):
#         while True:
#             print(multiprocessing.current_process())
#             print("进程:" + self.name)

# 进程一定要放在if __name__ == '__main__'下，它需要freeze_support()方法
# 根本原因：windows创建进程没有fork方法，默认是spawn，而linux创建进程默认是fork方法
# if __name__ == '__main__':
#     process1 = Process(target=task1, args=('task1...',), name='任务1')
#     process2 = Process(target=task2, args=('task2...',), name='任务2')
#     print(process1.name)
#     print(process2.name)
#     process1.start()
#     process1.join()
#     process2.start()
#     process2.join()
    # while True:
    #     time.sleep(1)
    #     n += 1
    #     print("主进程", n)
    #     # 自定义进程的main方法
    #     p1 = MyProcess('自定义进程1')
    #     p2 = MyProcess('自定义进程2')
    #     p1.start()
    #     p2.start()


# # 非阻塞式进程池
# # (1)全部添加到队列中，立刻返回，并没有等待其他进程执行完毕；
# # (2)回调函数等待进程任务完成才调用；
def task(name):
    print("任务:{} 进程id:{}".format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 2)
    end = time.time()
    return '任务完成！{} 进程id:{} 用时:{}'.format(name, os.getpid(), end - start)


def callback_fun(s):  # s相对于task(name)
    print(s)


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '看电影', '散步', '玩游戏', '吃东西', 'daw', 'ffde']
    for i in tasks:
        pool.apply_async(task, args=(i,), callback=callback_fun)
    pool.close()  # 参数传入完成后需要用close()方法关闭函数参数入口
    pool.join()  # 进程池会随着主进程的结束而结束，所以要用进程阻塞join()方法

    print('主进程结束')

# 阻塞式进程池
# (1)并没有体现进程的有点；
# (2)添加一个执行一个，新的任务执行必须等待当前的任务完成；
# def task(name):
#     print("任务:{} 进程id:{}".format(name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*2)
#     end=time.time()
#     # 与非阻塞式的差别点-1
#     print('任务完成！{} 进程id:{} 用时:{}'.format(name,os.getpid(),end-start))
#
# if __name__ == '__main__':
#     pool = Pool(5)  # 定义进程池可调度最大进程数
#     tasks = ['听音乐', '看电影', '散步', '玩游戏', '吃东西', 'extra_1', 'extra_2']
#     for i in tasks:
#         # 与非阻塞式的差别点-2
#         pool.apply(task, args=(i,))
#     pool.close()
#     pool.join()
#     print('主进程结束')
