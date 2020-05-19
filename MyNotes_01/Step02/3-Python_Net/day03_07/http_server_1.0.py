# author: Ziming Guo
# time: 2020/3/26
'''
    http_server 1.0
    将刚才的那个文件发送给客户端（浏览器）
    这是一个贯穿项目，第一版
    基本要求：
        1）获取来自浏览器的请求
        2）判断 如果请求内容是 / 就将 index.html 返回给客户端
        3）如果请求的是其他内容，就返回 404
'''

from socket import *


# 客户端(浏览器)处理函数
def request(connfd):
    # 获取请求，将请求的内容提取出来(参见请求格式)
    # 判断是 / 则返回 index.html ; 不是 / 则返回404
    # 把内容给浏览器的方法就是文件的处理方式，读取，然后发送
    recv01 = connfd.recv(1024)
    # 防止浏览器异常退出
    if not recv01:
        return
    str01 = recv01.decode().split(" ")
    if str01[1] == "/":
        with open('index.html')as f:  # with 打开的，所以不用关闭
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()  # 之前写的那个index就只是用作响应体，而不是整个响应
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry, there is no any content....</h1>"

    # 响应拼接完毕，要发送给浏览器
    connfd.send(response.encode())
    # sockfd.close()
    # connfd.close()
    # 也可以不写着两个 close ，可以循环的发起请求并给出响应


# 搭建tcp网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 属性的用法,让端口可以重复使用

sockfd.bind(('0.0.0.0', 8000))  # 绑定

sockfd.listen(3)  # 设置监听

while True:
    connfd, addr = sockfd.accept()
    print("Connect from", addr)
    request(connfd)  # 调用一个函数，用来处理客户端请求
