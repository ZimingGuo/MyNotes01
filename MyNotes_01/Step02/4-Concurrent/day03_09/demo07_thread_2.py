# author: Ziming Guo
# time: 2020/3/30
'''
    demo_thread
    线程的函数参数演示
    1)演示传参
    2)演示创建多个线程
'''

from threading import Thread
from time import sleep


# 含有参数的线程函数
def fun01(sec, name):
    print("线程函数的参数")
    sleep(sec)
    print("%s执行完毕" % name) # 抢占的关系，不一定是按照顺序进行的


# 同时创建多个线程
jobs = []  # 创建一个列表，专门用装不同的线程，方便之后对结束的线程进行处理
for i in range(5):
    t = Thread(target=fun01, args=(2,), kwargs={'name': 'T%d' % i})
    jobs.append(t) # 把线程对象存进来
    t.start()

for i in jobs: # 通过之前创建的列表处理每一个结束的线程
    i.join()
