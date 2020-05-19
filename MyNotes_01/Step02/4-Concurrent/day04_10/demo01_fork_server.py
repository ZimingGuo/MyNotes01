# author: Ziming Guo
# time: 2020/4/1
'''
    fork_server
    基于fork的多进程并发
    目标就是连接多个客户端，能够为多个客户端同时提供服务
    【重点代码】
    步骤如下：
    1. 创建监听套接字
    2. 等待接收客户端请求
    3. 客户端连接创建新的进程处理客户端请求（子进程）客户端发来的请求，是要子进程处理的【c】
    4. 原进程继续等待其他客户端连接（父进程）就是用来处理客户端连接的【s】不断 accept
    5. 如果客户端退出，则销毁对应的进程
'''

from socket import *
import os
# 因为之后是要用到 fork 的，所以要用到 os 库
import signal

# 调用 signal 用来处理僵尸进程

# 全局变量
HOST = '0.0.0.0'
POST = 8888
ADDR = (HOST, POST)


def handle(c):
    # 用来具体处理客户端请求
    # 现在这个没有实际意义，只是要长期占有服务器
    while True:
        data = c.recv(1024)  # 接收消息
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 这句话是设置套接字的端口重用，使这个端口可以立即重新使用
s.bind(ADDR)  # 绑定
s.listen(5)  # 设置监听

# 处理僵尸进程（只要是在父进程当中写了这一句，子进程之后就自然由操作系统进行处理了）
# 写了这一句就相当于是父进程放弃了处理子进程的权利
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("Listen the port 8888...")

# 下面就要开始等待客户端的连接了(注意是多个客户端的连接)
while True:
    # 循环用于多次处理/接收客户端连接
    try:
        c, addr = s.accept()  # 等待客户端连接
        print("Connect from", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 走到这一步证明已经有客户端连接上来了
    # 创建子进程处理客户端事物
    pid = os.fork()
    if pid == 0:
        # 子进程处理客户端的请求
        # 子进程就是用来发消息的，不需要 s 套接字来建立连接
        s.close()  # 在子进程中关闭了这个套接字，不会影响父进程的执行
        handle(c)  # 把处理客户端请求封装成一个函数，专门用来处理客户端请求
        os._exit(0)  # 执行完之后将子进程销毁
    else:
        # 父进程继续返回去
        # 无论是父进程还是 fork 出错，都需要回去继续处理连接
        c.close()  # 同理，在父进程中关闭了这个c，即客户端连接套接，也是没有影响的，因为这个 c 是给子进程用的
        # 父进程就是用来不断的接收客户端的连接，c 对他没有用，不需要和客户端进行沟通 or 通信
        pass
    # 子进程负责处理请求，父进程回来继续判断是否有客户端连接


# 总结：
# 实际上我们可以创建多个客户端，父进程为每一个客户端创建了一个子进程
# 中心思想就是一个进程专门用来建立连接，另外一个进程专门用来处理事物