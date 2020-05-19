# author: Ziming Guo
# time: 2020/4/4
'''
    demo01:
    block_io
    socket 套接字非阻塞示例
    写一个 tcp 的服务端，不断等待连接，要是没有连接，每隔三秒就填充一个日志
'''

from socket import *
from time import ctime, sleep

# 日志文件
f = open('log.txt', 'a+')

# 创建一个 tcp 套接字
sockfd = socket()
sockfd.bind(('127.0.0.1', 8888))
sockfd.listen(3)

# 设置套接字为非阻塞
# 这句话的含义就是，以后所有通过 sockfd 调用的所有函数，都不会阻塞
# sockfd.setblocking(False)

# 设置超时检测
sockfd.settimeout(3)  # 设置超时检测，最多等待3秒

# 循环等待客户端的连接
while True:
    print("Waiting for connection...")
    # 这里原本是一个阻塞的行为
    # 虽然通过 setblocking 设置成了非阻塞，但执行到这里的时候还是会报错
    # 所以 每有客户端连接，每隔三秒写一条日志
    try:
        connfd, addr = sockfd.accept()
    except (BlockingIOError, timeout) as e: # 同时捕获多个异常的时候要加括号
        sleep(3)
        f.write("%s : %s\n" % (ctime(), e))
        f.flush()  # 刷新一下缓冲区
    else:
        print("Connect from", addr)
        data = connfd.recv(1024).decode()
        print(data)
