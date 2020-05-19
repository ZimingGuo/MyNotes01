# author: Ziming Guo
# time: 2020/4/1
'''
    练习1：
    根据 fork 的多进程并发网络模型思路
    完成基于 Process 的多进程并发网络模型
    （就相当于是用 Process 创建多进程没但是最终的结果现象适合原来 fork 的时候是一样的）

    步骤：
    1. 创建监听套接字
    2. 等待接收客户端请求
    3. 客户端连接创建新的进程处理客户端请求（子进程）客户端发来的请求，是要子进程处理的【c】
    4. 原进程继续等待其他客户端连接（父进程）就是用来处理客户端连接的【s】不断 accept
    5. 如果客户端退出，则销毁对应的进程
'''

from multiprocessing import Process
from socket import *
import os
import signal

HOST = '0.0.0.0'
POST = 9999
ADDR = (HOST, POST)
list_process = []

# 创建 tcp 套接字
s01 = socket()
s01.bind(ADDR)
s01.listen(1024)

# 设置套接字立即重用
s01.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 防止僵尸进程的出现
# 这种方法也可以用在 multiprocessing 当中处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("Listen the port 8888...")


def fun01(connfd, s01):
    s01.close()
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'OK')
    connfd.close()  # 关闭
    os._exit(0)


while True:
    try:
        connfd, addr = s01.accept()
        print("Connected from", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    p01 = Process(target=fun01, args=(connfd, s01))
    # p01.daemon = True  # 这句话的意思就是，父进程结束，所有进程终止
    list_process.append(p01)
    p01.start()
    # 提示一下：这个 join 一定不能写在 while 循环里面
    # 因为 join 是一直阻塞到这个进程执行结束的
    # 这样一来，必须要第一个连接断开了才可以连接下一个客户，违背了初始想法

    # 父进程-建立连接
    connfd.close()

for item in list_process:
    item.join()
