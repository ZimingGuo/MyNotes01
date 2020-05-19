# author: Ziming Guo
# time: 2020/3/30
'''
    dmeo_thread:
    线程基础实用演示
    步骤：基本同 process
    1）封装线程函数
    2）创建线程对象
    3）启动线程
    4）回收线程
'''

import threading
from time import sleep
import os

a = 1


# 编写线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(), "播放:大海啊 故乡")
    global a
    print("a = ", a)
    a = 10000


# 创建线程对象
t = threading.Thread(target=music)

t.start()  # 启动线程

for i in range(4):
    sleep(1)
    print(os.getpid(), "再播放一首歌:咿呀咿")

t.join()  # 回收线程
print("a is ", a)  # 最终却是 10000，因为在线程中，一共就一个进程，只要是改了一个变量的值，整个进程的变量值都会被改变
# 在进程中，这个 a 还会是 1，因为子进程是直接 copy 了父进程代码，该变量的值改的是子进程自己的，所以父进程不会改变

# 这一大堆的代码是含有两个线程的，主线程 和 分支线程
# 分支线程是 music 这个函数里的内容
# 分支线程只是执行这个函数，而其他的内容都是由主线程执行的
# 各自的线程运行各自的，相互之间不受影响

# 以上打印出来的 pid 的号码是一样的，因为这些线程都是在一个进程内执行的

# all in all 进程和进程之间是相互独立的空间，而线程是在进程当中的一部分，读取 or 修改的都是全局变量
