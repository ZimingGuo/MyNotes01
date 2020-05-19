# author: Ziming Guo
# time: 2020/3/31
'''
    demo thread_lock
    线程锁的演示
'''

from threading import Thread, Lock

a = b = 0
lock = Lock() # 定义锁


def value():
    while True:
        lock.acquire() # 上锁
        if a != b:
            print("a = %d, b = %d" % (a, b))
        lock.release() # 解锁


t = Thread(target=value)

t.start()

while True:
    with lock: # 用 with 语句块上锁，with 执行完之后解锁
        a += 1
        b += 1

t.join()

# 能够打印出来结果的原因是：
#   主线程和分支线程是同时运行的，肯定在某一时刻，a 加了1，b 还没来得及加
#   每当这个时候，就不相等，就可以打印了
