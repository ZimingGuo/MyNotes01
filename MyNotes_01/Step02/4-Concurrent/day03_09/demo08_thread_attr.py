# author: Ziming Guo
# time: 2020/3/30
'''
    demo_thread_attr
    演示线程的属性
'''

from threading import Thread
from time import sleep


def fun01():
    sleep(3)
    print("线程属性测试")


t = Thread(target=fun01, name='Hahaha')

t.setDaemon(True)  # 加上这个就是让主线程结束之后，子线程也要马上结束，没完事也要结束
# 让主进程随着分支进程的退出而退出

t.start()  # 主线程的执行结束并不影响子线程的执行

t.setName('Lueluelue')
print(t.getName())
print('is alive:', t.is_alive())
print('daemon:', t.isDaemon())
