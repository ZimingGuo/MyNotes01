# author: Ziming Guo
# time: 2020/3/29
'''
    Process 的参数传递方法
'''

from multiprocessing import Process
from time import sleep


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working now")


# 把上面的这个函数变成一个进程
# p = Process(target=worker, args=(2, 'Jasson'))  # 用 args 的方式传参
p = Process(target=worker, kwargs={'name': 'Jacky', 'sec': 2})

p.start()
p.join()
