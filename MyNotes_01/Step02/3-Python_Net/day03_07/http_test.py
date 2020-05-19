# author: Ziming Guo
# time: 2020/3/25
'''
    http 请求响应测试
    就相当于写了一个服务端，客户端是浏览器
'''

from socket import *


s = socket()  # 创建套接字
s.bind(('0.0.0.0', 8001))  # 绑定
s.listen(3)  # 监听

c, addr = s.accept()  # 等待客户端连接
print("Connected from", addr)
data = c.recv(4096)  # 接收消息
print(data)

# 了解响应格式
response="""HTTP/1.1 200 OK
Content-Type:text/html 

<h1>Hello World</h1>
""" # """ 的意思表示文档，可以当作多行注释；
# 还是一个固定格式的字符串，这个和一般的字符串不同，一般的字符串是要手动 /r 换行的

c.send(response.encode())

c.close()  # 关闭连接套接字
s.close()  # 关闭套接字
