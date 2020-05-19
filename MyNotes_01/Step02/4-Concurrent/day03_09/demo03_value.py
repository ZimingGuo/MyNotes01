# author: Ziming Guo
# time: 2020/3/30
'''
    demo_value:
    value  开辟单一共享内存空间
    注：共享内存中只能有一个值
'''

from multiprocessing import Process, Value
import time
import random

# 创建一个共享内存
money = Value('i', 5000)  # 表示存的是整数，初始值的 5000


# 操作共享内存
def main():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1, 1000)  # 对共享内存的内容写


def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= random.randint(100, 800)  # 对共享内存的内容写


p1 = Process(target=main)
p2 = Process(target=girl)

# 开启两个进程
# 这两个进程操作的是同一块共享内存
p1.start()
p2.start()

# 回收两个进程
p1.join()
p2.join()

# 获取共享内存的数据
print("一个月的余额:", money.value)  # 对共享内存的内容读

# 两个子进程进行的是一个写操作，父进程做的是一个读操作
