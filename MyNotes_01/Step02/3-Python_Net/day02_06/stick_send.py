# author: Ziming Guo
# time: 2020/3/18
'''
    stick_send 粘包发送端演示
'''

from socket import *
from time import *

sockfd = socket()

server_addr = ('127.0.0.1', 8889)
sockfd.connect(server_addr)

while True:
    sleep(0.3) # 每隔0.3秒发送一次，明显发送速度大于接收速度
    sockfd.send(b'hahaha')
