# author: Ziming Guo
# time: 2020/3/18
'''
    tcp_client
    重点代码
'''
from socket import *

# 创建tcp套接字
sockfd = socket()  # 使用默认参数就是tcp套接字

# 通常客户端不写绑定(bind)，因为存在一定风险的，还是让系统自己分配吧

# 连接服务器
server_addr = ('127.0.0.1', 8888)  # 端口是要保持一致的，这是服务端地址
sockfd.connect(server_addr)

while True:  # 一直循环
    # 收发消息（先发后收，因为服务端是先收后发）
    data = input("Input a message")
    if not data:
        break
    sockfd.send(data.encode())  # 此处注意：一定要是字节码的形式
    data = sockfd.recv(1024)
    print("Server:", data.decode())  # 转化成字符串

# 关闭套接字
sockfd.close()
