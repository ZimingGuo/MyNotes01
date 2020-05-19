# author: Ziming Guo
# time: 2020/4/1
'''
    demo03：
    thread_server 基于 threading 的多线程并发
    步骤：
    1. 创建监听套接字
    2. 循环接收客户端连接请求
    3. 当有新的客户端连接创建线程处理客户端请求
    4. 主线程继续等待其他客户端连接
    5. 当客户端退出，则对应分支线程退出
'''

from threading import Thread
from socket import *
import os, sys


# 处理具体客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


# 设置全局变量
HOST = '0.0.0.0'
POST = 8888
ADDR = (HOST, POST)

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

print("Listen the port 8888......")

# 循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e)
        continue

    # 创建线程处理请求（如果有客户端要求连接，就要创建新的线程）
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True)  # 作用是 一旦主线程退出了，所有分支线程都应该随之退出
    t.start()
    # 在这之后，主线程应该是直接回到 while 循环，等待创建下一个循环
    # 具体的请求是由分支线程调用一个函数来处理
