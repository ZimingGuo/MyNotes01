# author: Ziming Guo
# time: 2020/3/19
'''
    demo_else:
        套接字属性介绍
'''

from socket import *

# 创建套接字
s = socket()

# 设置端口可以立即重新使用，在绑定地址之前
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 最后一个value写1或者写true都是一样的

s.bind(('192.168.101.4', 8888))
s.listen(3)
c, addr = s.accept()  # 阻塞函数，如果不连接就一直被阻塞

print("地址类型：", s.family)
print("套接字类型：", s.type)
print("绑定地址：", s.getsockname())  # 当前还没有绑定任何地址
print("文件描述符", s.fileno())

# 结果同 accept 返回的 addr
print("连接端地址", c.getpeername())  # 无法获取的，不同套接字拥有不同的属性和功能
# getpeername 必须要由连接套接字调用才可以
# 实际上打印出来的结果就是 addr
