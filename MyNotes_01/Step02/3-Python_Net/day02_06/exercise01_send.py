# author: Ziming Guo
# time: 2020/3/18
'''
    exercise02_send
'''
from socket import *

sockfd = socket()

address = ('127.0.0.1', 9999)
sockfd.connect(address)

# 读取目标文件，循环发送
openfile = open('test_file.txt', 'rb')
while True:
    sending_file = openfile.read(10)
    if not sending_file:
        break
    sockfd.send(sending_file)

print("all sent")

data01 = sockfd.recv(1024)
print(data01.decode())

openfile.close()
sockfd.close()
