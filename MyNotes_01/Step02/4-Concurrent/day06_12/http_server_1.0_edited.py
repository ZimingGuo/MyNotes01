# author: Ziming Guo
# time: 2020/3/26

from socket import *


# 处理客户端请求
def request(connfd):
    # 直接获取HTTP请求
    data = connfd.recv(4096)
    # 防止浏览器断开
    if not data:
        return

    # 提取请求内容
    request_line = data.decode().split('\n')[0]
    info = request_line.split(' ')[1]

    # 判断请求内容是否为 /
    if info == '/':
        with open('index.html') as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry....</h1>"
    # 发送给浏览器
    connfd.send(response.encode())

    sockfd.close()
    connfd.close()


# 搭建tcp服务
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('0.0.0.0', 8080))
sockfd.listen(5)
while True:
    connfd, addr = sockfd.accept()
    print("Connect from", addr)
    request(connfd)  # 具体处理客户端请求
