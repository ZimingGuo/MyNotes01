# author: Ziming Guo
# time: 2020/3/18
'''
    exercise01_recv
'''
from socket import *

sockfd = socket()  # 创建对象

sockfd.bind(('0.0.0.0', 9999))  # 绑定

sockfd.listen(5)  # 设置监听

connfd, addr = sockfd.accept()
print("连接成功")

# 接收文件思路：打开新文件；一边接受一边写入（循环接受写入）
# 打开文件
creat_file = open('to_write.txt', 'wb')
# 循环接收写入,记住一定是循环写入
while True:
    received_file = connfd.recv(1024)
    if not received_file:
        break
    creat_file.write(received_file)

    to_say = "已写完"
    n = connfd.send(to_say.encode())
print("任务完成")

creat_file.close()
sockfd.close()
connfd.close()
