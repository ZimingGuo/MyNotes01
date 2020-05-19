# author: Ziming Guo
# time: 2020/3/27

from socket import *
import struct

ADDR = ('127.0.0.1', 8899)

sockfd = socket(AF_INET, SOCK_DGRAM) # 创建udp套接字
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

while True:
    stu_info = input("请输入学生信息，id-name-age-score，要用'-'分隔开")
    if not stu_info:
        break
    list_info = stu_info.split('-')
    st01 = struct.Struct('i4sif')
    packed_info = st01.pack(int(list_info[0]), list_info[1].encode(), int(list_info[2]), float(list_info[3]))
    # 打包数据并发送，pack 完直接就是字节串

    sockfd.sendto(packed_info, ADDR)

    data, addr_recv = sockfd.recvfrom(1024)
    print(data.decode())

sockfd.close()
