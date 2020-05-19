# author: Ziming Guo
# time: 2020/3/30
'''
    demo02_queue:
    消息队列演示
    注：消息队列符合先进先出的原则
'''

from multiprocessing import Queue, Process
from time import sleep
from random import randint

# 创建消息队列
q = Queue(5)


def handle():  # 第一个子进程
    for i in range(6):
        x = randint(1, 33)
        q.put(x)  # 向消息队列里面添加内容
    q.put(randint(1, 16))


def request():  # 第二个子进程
    while True:
        print("摇啊摇")
        sleep(2)
        try:
            print(q.get(block=True, timeout=3), end=' ')
        except:
            break


'''
def request():  # 第二个子进程
    l = []
    for i in range(6):
        l.append(q.get())
    l.sort()
    l.append(q.get())
    print(l)
'''

p1 = Process(target=handle)
p2 = Process(target=request)

# 开启两个进程
p1.start()
p2.start()

# 回收两个进程
p1.join()
p2.join()
