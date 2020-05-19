# author: Ziming Guo
# time: 2020/3/28
'''
    demo: 获取 PID 的值
'''

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:  # 子进程
    sleep(2)
    print("Child ID is", os.getpid())  # 获取子进程的 pid 值
    print("Parent ID is", os.getppid())  # 获取父进程的 pid 值
else:  # 父进程
    print("Get child PID", pid)  # 在父进程里获取子进程 pid 就是直接打印 pid
    print("Parent PUD", os.getpid())  # 在父进程中获取父进程(自己)的 pid
