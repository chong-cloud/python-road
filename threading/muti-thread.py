import sys
import threading
import time


# 返回当前活跃线程的数量
print(threading.active_count())
# 返回当前的线程变量,即 当前线程对象
print(threading.currentThread())
# 返回一个包含正在运行的线程的list
print(threading.enumerate())
"""
python解释器中有GIL锁，每执行100行代码就释放GIL锁，让别的线程有机会执行，所以python永远最多使用1个CPU核心，若想要多核需要拓展C代码
run(): 用以表示线程内进行的活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。
"""

# 多线程创建方式1，指定run的方法运行哪个函数
# def calculate_number():
#     print(12)
# t = threading.Thread(target=calculate_number)
# t.start()

# threading自定义线程
exitFlag = 0


class myThread (threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)
        # 加锁
        lock.acquire()
        # 解锁
        lock.release()


def print_time(threadName, delay, counter):
    while counter:
        # if exitFlag:
        #     # 如何退出线程
        #     threading.Thread._stop(threading.currentThread())
        time.sleep(delay)
        print("%s: %s :%s" % (threadName, threading.currentThread().name, time.ctime(time.time())))
        counter -= 1


lock = threading.Lock()

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
#将thread1设置为守护线程,所有线程结束后，无论守护线程是否运行结束，都强制结束。例如：垃圾回收机制
thread1.daemon = True

thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

# 直接创建线程
t = threading.Thread(target=print_time, args=("testk", 1, 6), name="测试线程")
t.start()

# 获得线程的局部变量
tk = threading.local()
def aa():
    print("bb", tk.student)

def bb():
    tk.student = "schoo"
    print("这是bb方法")
    aa()

# a = threading.Thread(target=aa, name="aa")
b = threading.Thread(target=bb, name="bb")
# a.start()
# a.join()
b.start()


# # 锁示例
# my_list = []
#
#
# def kk():
#     for i in range(50):
#         # with lock:
#         my_list.append("aa")
#         my_list.append("aa2")
#         print(threading.currentThread().name, "  list:  ", my_list)
#
#
# t1 = threading.Thread(target=kk, name="Threading1")
# t2 = threading.Thread(target=kk, name="Threading2")
#
# t1.start()
# t2.start()

# # 线程池
# from concurrent.futures import ThreadPoolExecutor
#
#
# def task1(max_sum):
#     sums = 0
#     for k in range(max_sum):
#         print("线程名:", threading.current_thread().name, k)
#         sums += 1
#     return sums
#
#
# # 设置线程池最大线程数
# pool = ThreadPoolExecutor(20)
# futures = []
# # 提交两个参数
# for i in [50, 100]:
#     # 将线程放入futures列表
#     futures.append(pool.submit(task1, i))
# # 遍历futures列表查看执行情况与返回值
# for j in futures:
#     print(j.done())
#     print("结果:", j.result())
