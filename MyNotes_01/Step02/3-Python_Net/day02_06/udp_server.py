# author: Ziming Guo
# time: 2020/3/18
'''
udp 服务器
重点代码
'''
from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1', 8888)
sockfd.bind(server_addr)

# 循环收发消息
while True:
    data, addr = sockfd.recvfrom(1024)
    print("收到消息:", data.decode())
    sockfd.sendto(b'Thanks', addr)  # 这个地方传addr的原因是，谁给我发消息我就给谁回复消息

# 关闭套接字
sockfd.close()

# udp的测试只能自己搭客户端，不能用 telnet，因为telnet只是tcp情况下的模拟程序
# 客户端的断开，客户端的结束，和服务端没有任何关系，因为是udp
# udp没有连接，没有三次握手四次挥手
