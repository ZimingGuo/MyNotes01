# author: Ziming Guo
# time: 2020/3/29
'''
    demo Process 的几个属性
'''
from multiprocessing import Process
import time


def tm():
    for i in range(3):
        time.sleep(2)
        print(time.time())


p = Process(target=tm, name='Haha')

p.daemon = True  # 再有的程序里面，希望主进程结束之后，其他进程也随之结束，这时就会用到 daemon

p.start()
print("Name:", p.name)  # 打印进程名称，也可以重新赋值
print("PID:", p.pid)  # 对应子进程的PID
print("is alive:", p.is_alive())  # 判断p的进程是否在生命周期
