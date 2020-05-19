# author: Ziming Guo
# time: 2020/3/25
'''
    发送广播
    1）创建 udp 套接字
    2）设置可以发送广播
    3）循环向广播地址发送
'''
from socket import *
from time import *

# 广播地址
dest = ('192.168.101.255', 9999)

# 创建数据报套接字
s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# 发送内容
data = '哈哈哈哈哈哈哈哈，呦吼'

while True:
    sleep(2)
    s.sendto(data.encode(), dest)  # 目标地址 = 广播地址
