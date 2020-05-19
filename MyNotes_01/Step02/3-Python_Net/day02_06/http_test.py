# author: Ziming Guo
# time: 2020/3/25
'''
    http 请求响应测试
'''

from socket import *

# 写一个 tcp 服务端
# tcp套接字，因为 http 使用 tcp 传输
s = socket()  # 创建套接字
s.bind(('0.0.0.0', 8000))  # 绑定
s.listen(3)  # 监听

c, addr = s.accept()  # 等待客户端连接
print("Connected from", addr)
data = c.recv(4096)  # 接收消息
print(data)
# 这个地方打印的就是 http 请求
# 客户端和浏览器连接上之后会直接发送一个连接请求
# 就收到的这个请求是符合 http 请求格式的：请求行/头/空行/体

c.close()  # 关闭连接套接字
s.close()  # 关闭套接字
