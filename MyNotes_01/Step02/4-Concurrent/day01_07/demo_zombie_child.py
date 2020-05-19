# author: Ziming Guo
# time: 2020/3/28
'''
    demo
    用二级子进程的方式防止僵尸进程的产生
    避免的 wait 方法的缺点
'''

import os, sys
from time import sleep


def fun01():
    for i in range(3):
        sleep(2)
        print("写代码")


def fun02():
    for i in range(2):
        sleep(4)
        print("测代码")


pid = os.fork()
if pid < 0:
    print("Error")



elif pid == 0:  # 一级子进程
    pid02 = os.fork()
    if pid02 < 0:
        print("Error")
    elif pid02 == 0:  # 二级子进程
        fun01()
        print("fun01执行完毕")
    else: # （二级的父进程）还是一级子进程
        print("还是一级子进程")
        os._exit(0) # 让一级子进程赶紧退出，二级子进程是真正发挥作用的



else:  # 父进程
    os.wait() # 等待一级子进程结束，用来处理一级子进程的僵；但这个会很快结束，因为真正有用的是二级子进程
    fun02()
    print("fun02执行完毕")
