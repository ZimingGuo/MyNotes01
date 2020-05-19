# author: Ziming Guo
# time: 2020/3/27
'''
    练习：
    使用udp完成 学生信息录入系统
    客户端不断录入学生信息，将信息发送到服务端
    在服务端将学生信息写入到一个文件中，每个学生信息占一行

    信息格式： id(int)  name(str)  age(int)  score(float)
'''
from socket import *
import struct

file_stuinfo = open('stu_info.txt', 'ab+')

sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sockfd.bind(('0.0.0.0', 8899))

while True:
    st02 = struct.Struct('i4sif') # 这个两端的打包格式必须相同
    data, addr_send = sockfd.recvfrom(1024) # 接收
    if not data:
        break
    print("already received")
    sockfd.sendto(b'Thanks', addr_send)
    final_info = str(st02.unpack(data))
    file_stuinfo.write(final_info.encode())  # 写入
    file_stuinfo.flush() # 这里是一个很巧妙的设计，要刷新一下

sockfd.close()
file_stuinfo.close()
