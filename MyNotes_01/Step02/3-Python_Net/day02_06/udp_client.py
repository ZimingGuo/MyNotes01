# author: Ziming Guo
# time: 2020/3/18
'''
udp客户端代码
重点代码
'''
# 收发也要相呼应，因为也有阻塞

from socket import *

# 服务端地址
ADDR = ('127.0.0.1', 8888) # 这个地址就是client发送的目标地址，给这个地址发消息，服务端就接收到了

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 无绑定地址

# 循环收发消息
while True:
    data = input("输入：")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)  # 这个应该发送给服务器，所以地址是服务器的地址，目标地址
    msg, addr = sockfd.recvfrom(1024)
    print("From server:", msg.decode())

# 关闭套接字
sockfd.close()

# 如果只运行客户端，发出来一条消息，如果没有人接收，那就丢失了，但是不会报错的，因为是udp
# 而且开启几个客户端都可以，原因就是没有连接
# 对于服务端来说，谁给我发都行，谁给我发我就回复谁，不管是谁发的，有目标地址在呢
