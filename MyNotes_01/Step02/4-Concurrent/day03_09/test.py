# author: Ziming Guo
# time: 2020/3/31
'''
    测试用例
'''


# 这是一个典型的计算密集型程序
def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


# 用单进程执行 10 遍，记录执行时间（时间差）
# 用多进程执行：十个进程，每个进程执行一遍
# 用多线程执行：十个线程，每个线程执行一遍


# 写一个无阻塞的IO行为
# 用单进程执行 10 遍，记录执行时间（时间差）
# 用多进程执行：十个进程，每个进程执行一遍
# 用多线程执行：十个线程，每个线程执行一遍
def io():
    write()
    read()


def write():
    f = open('test', 'w')
    for i in range(1800000):
        f.write("Hello World\n")
    f.close()


def read():
    f = open('test')
    lines = f.readlines()
    f.close()
