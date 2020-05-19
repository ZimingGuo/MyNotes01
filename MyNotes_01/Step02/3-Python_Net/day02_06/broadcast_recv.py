# author: Ziming Guo
# time: 2020/3/25
'''
    广播接收端
    1）创建udp
    2）设置套接字可以发送接收广播（setsockopt）依赖于这个函数，并不是所有的套接字都能够发送or接收广播
    3）选择接收的端口
    4）接收广播
'''
# 流程比较固定

from socket import *

s = socket(AF_INET, SOCK_DGRAM)

# 设置套接字接收广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # 表示这个套接字可以接收广播

s.bind(('0.0.0.0', 9999))  # 这个端口的设置就好比选台一样

while True:
    msg, addr = s.recvfrom(1024) # 这个位置，udp的接收，只能是二进制的格式
    print(msg.decode())
