# author: Ziming Guo
# time: 2020/3/18
'''
stick_recv 演示
'''

from socket import *
from time import *

# 创建tcp套接字
sockfd = socket()

# 绑定地址
sockfd.bind(('0.0.0.0', 8889))

# 设置监听
sockfd.listen(5)

connfd, addr = sockfd.accept()

while True:
    sleep(1)  # 每隔一秒接收一次
    data = connfd.recv(1024)
    print(data.decode())
