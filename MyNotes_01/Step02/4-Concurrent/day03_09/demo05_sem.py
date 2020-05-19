# author: Ziming Guo
# time: 2020/3/30
'''
    demo_sem:
    信号量演示
    思路：信号量的数量，相当于资源
    执行任务就必须要消耗资源
'''

from multiprocessing import Process, Semaphore
from time import sleep
import os

# 创建信号量
sem = Semaphore(3)  # 表示资源就只有三个


# 任务函数
def handle():
    sem.acquire()  # 想要执行任务就必须消耗一个信号量(一共就三个)
    print("%s 执行任务" % os.getpid())
    sleep(2)
    print("%s 执行任务完毕" % os.getpid())
    sem.release()  # 执行完任务之后再释放一个任务量


# 10个任务需要执行
for i in range(10):
    p = Process(target=handle)
    p.start()

# 正常情况下，不加 acquire 的话就是会同时执行10个进程，但是有的时候系统会受不了
# 加上了 acquire 之后就有了限制，每次只能最多三个进程一起执行，一批一批来
