# author: Ziming Guo
# time: 2020/3/18
'''
    demo01：
        tcp_server
        重点代码
    注意：
    功能性代码，注意流程和函数的使用
'''
import socket

# 创建TCP套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 什么参数都不传实际上就是创建TCP套接字


# 绑定地址
sockfd.bind(('0.0.0.0', 8887))

# 设置监听
sockfd.listen(5)

while True:  # 这个循环的条件就是防止，客户端推出之后服务器也跟着推出，正常应该服务器一直在线，等待其他客户端的连接
    # 阻塞等待处理连接，有两个返回值
    print("waiting for connecting...")
    connfd, addr = sockfd.accept()  # 正常来说这句话就是连接，不会有任何现象，前后加上 print 是为了看到现象
    print("Connect from", addr)
    while True:
        # 收发消息
        data = connfd.recv(1024)  # 收
        if not data:  # 如果date为空，说明客户端已经退出
            break
        print("收到：", data.decode())
        n = connfd.send(b'Thanks')  # 注意，必须是一个字节串
        print("发送了%d字节" % n)

    connfd.close()

# 关闭套接字，两个套接字就要关闭两个
# 关闭一个 connfd 仔关闭一个 sockfd
sockfd.close()
