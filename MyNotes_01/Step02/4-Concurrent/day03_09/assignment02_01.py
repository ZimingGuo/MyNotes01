# author: Ziming Guo
# time: 2020/3/31
'''
    作业2_1：
    测试 进程 线程 但进程的执行效率（见test）
    检测：对于计算密集型的过程，三者的效率各是多少
'''

import time
from multiprocessing import Process
from threading import Thread


# 计算密集型程序
def count(x, y):
    c = 0
    while c < 1000000:
        x += 1
        y += 1
        c += 1


# 用单进程执行 10 遍，记录执行时间（时间差）
time01 = time.time()
for i in range(9):
    count(0, 0)
time02 = time.time()
sub01 = time02 - time01
print(sub01)

# 用多进程执行：十个进程，每个进程执行一遍
ls01 = []  # 创建一个列表存储各个进程
time03 = time.time()
for i in range(9):
    p01 = Process(target=count, args=(0, 0))
    ls01.append(p01)
    p01.start()
for item in ls01:
    item.join()
time04 = time.time()
sub02 = time04 - time03
print(sub02)

# 用多线程执行：十个线程，每个线程执行一遍
ls02 = []  # 创建一个列表存储各个线程
time05 = time.time()
for i in range(9):
    t01 = Thread(target=count, args=(0, 0))
    ls02.append(t01)
    t01.start()
for item in ls02:
    item.join()
time06 = time.time()
sub03 = time06 - time05
print(sub03)
