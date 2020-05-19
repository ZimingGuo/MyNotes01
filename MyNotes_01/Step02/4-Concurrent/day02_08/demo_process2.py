# author: Ziming Guo
# time: 2020/3/29
'''
    multiprocessing 创建多个进程
'''
from multiprocessing import Process
from time import sleep
import os


def fun01():
    sleep(3)
    print("吃饭")
    print(os.getppid(), '--', os.getpid())


def fun02():
    sleep(2)
    print("睡觉")
    print(os.getppid(), '--', os.getpid())


def fun03():
    sleep(4)
    print("敲代码")
    print(os.getppid(), '--', os.getpid())


# 把这三个事都变成循环

functions = [fun01, fun02, fun03]
list01 = []
for fun in functions:  # 通过循环遍历，一下子生成多个子进程，各自做自己的事情
    p = Process(target=fun)
    list01.append(p)
    p.start()
    # 这里不能写 join 不然就要等到每一件事都执行完才能执行在一个，就失去意义了

for i in list01:  # 通过列表将进程对象保存，到后面再一起回收
    i.join()

# 综上 一共四个进程，一个父进程，三个子进程
# 通过打印 pid 的值，可以知道这三个子进程都是一个父进程
