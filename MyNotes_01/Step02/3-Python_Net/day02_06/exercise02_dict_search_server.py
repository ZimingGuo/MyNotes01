# author: Ziming Guo
# time: 2020/3/19
'''
    exercise02_dict_search_server
'''

from socket import *
import dict_search_module

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_address = ('127.0.0.1', 8888)
sockfd.bind(server_address)

# 消息收发
while True:
    data, addr = sockfd.recvfrom(1024)
    explain = dict_search_module.searching_voca(data.decode())
    if not explain:
        print("already checked")
        sockfd.sendto(b'the word do not exsit', addr)
        print("already sent")
        continue
    else:
        print("already checked")
        sockfd.sendto(explain.encode(), addr)
        print("already sent")

sockfd.close()
