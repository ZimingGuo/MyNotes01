# author: Ziming Guo
# time: 2020/4/7
'''
    demo04:
    gevent_server 基于协程的 tcp 并发
    思路：
    1）将每个客户端的处理设置成协程函数，这样方便我们处理的时候进行跳转
    2）让 socket 模块下的阻塞可以触发协程跳转
    主体思想：在刚开始讲 tcp 的时候用的那个普通的循环模型基础上，把处理客户端的部分封装成函数
'''

import gevent
from gevent import monkey
monkey.patch_all() # 执行脚本，修改 socket 阻塞，此时所有的 socket 阻塞行为都变成了可以触发协程的阻塞

from socket import *


def handle(c):
    while True:
        data = c.recv(1024).decode() # 到了 recv 这里也是阻塞，就变成了哪个recv不阻塞，就执行哪一个
        if not data:
            break
        print(data)
        c.send(b'OK')


# 先写一个普通的 tcp 套接字模型
# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建完套接字下一步就是循环，循环接收客户端连接
while True:
    c, addr = s.accept() # 这个地方就可以触发协程，就可以跳到 handle 里面
    print("connected from", addr)  # 每当连接上一个客户端，就打印一下客户端地址
    # handle(c)  # 把循环收发消息封装成一个函数，handle 用来处理具体的客户端请求
    # 在当前的这个模型下，如果一个客户端连接进来后，就不能再连接一个客户端进行下一个接收了
    gevent.spawn(handle,c)