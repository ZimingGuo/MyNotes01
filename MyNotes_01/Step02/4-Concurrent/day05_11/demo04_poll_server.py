# author: Ziming Guo
# time: 2020/4/4
'''
    demo04:
    poll_server 完成 tcp 并发服务
    思路分析：借鉴 IO 多路复用
    建立 "fileno & IO对象" 的字典，用于 IO 查找
    步骤：
    【1】 创建套接字
    【2】 将套接字register
    【3】 创建查找字典，并维护
    【4】 循环监控IO发生
    【5】 处理发生的IO
'''
from socket import *
from select import *

# poll 的方法其实也是在 select 下的，不要记错

# 创建监听套接字，作为关注的 IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建 poll 对象
p = poll()

# 建立查找字典，通过一个 IO 的 fileno 的找到 IO 对象
# 以一个 IO 对象的文件描述符为键，以这个对象本身为值
fdmap = {s.fileno(): s}  # 必须始终和 register 的 IO 保持一致

# 关注 s（关注IO）
p.register(s, POLLIN | POLLERR)  # 关注 s 的两个事件
# 当这两个事件中的一个发生的时候，就会给返回值
# 当这个括号里面不传参数的时候，表示监视这个套接字的所有事件

# 循环监控 IO 发生
while True:
    events = p.poll()  # 这是一个阻塞函数，是用来监控 IO 事件发生的，监控的就是 register 的 IO 事件
    # print(events)  # 打印的结果应该是一个列表，列表里的每一个元素都是一个元组，代表发生的 IO 事件

    # 循环遍历列表，查看哪一个 IO 是就绪的，然后处理
    for fd, event in events:
        # 区分哪个 IO 就绪了
        # 如果是 s 就绪了的话
        if fd == s.fileno():  # fd 本身就是一个文件描述符，二者相等就说明就绪了
            c, addr = fdmap[fd].accept()  # 就相当于是用一个文件描述符来追溯一个对象
            print('Connected from', addr)
            # 关注新的客户端连接套接字
            p.register(c, POLLIN | POLLERR) # 此处的就绪情况可能是 POLLIN 也可能是 POLLERR
            fdmap[c.fileno()] = c  # 维护字典，每次多监视一个客户端就要把这个客户端的文件描述符放入字典，方便以后的遍历
        elif event & POLLIN:  # 判断是否为 POLLIN 就绪
            # 通过按位与的操作可以检查特定的过程是否就绪，这是按位与的特点
            data = fdmap[fd].recv(1024).decode()  # 还是通过文件描述符找到要相应的对象
            if not data:
                p.unregister(fd)  # 取消关注，这里填文件描述符或者文件对象都可以
                fdmap[fd].close()
                del fdmap[fd] # 结束关注/监视之后，要从字典里删除
                continue
            print(data)
            fdmap[fd].send(b'OK')


# 基本思想：监控多个 IO ，哪个 IO 发生了我就去处理哪个 IO
#          两次关注，第一次 s 第二次 c
# 其实 select 和 poll 的基本思想是没有变的，只不过现在是创建了一个对象，通过对对象的调用，来完成监控
