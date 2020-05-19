# author: Ziming Guo
# time: 2020/3/19
'''
    exercise02_dict_search_client
'''
from socket import *

# 创建地址
ADDR = ('127.0.0.1', 8888)

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

while True:
    voca = input("请输入要查找的单词:")
    if not voca:
        break
    sockfd.sendto(voca.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("Explain from server:", msg.decode())

sockfd.close()
