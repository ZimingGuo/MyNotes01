# author: Ziming Guo
# time: 2020/4/4
'''
    dmeo03:
    select tcp 服务端
    tcp 套接字 IO 并发模型

    思路分析：
    1）将关注的IO放入到监控列表中中
    2）当 IO 就绪的时候会通过 select 返回
    3）遍历返回值列表，然后得知哪个 IO 就绪，再进行处理
'''

from socket import *
from select import select

# 创建监听套接字作为关注的IO
s = socket() # 这个创建的监听套接字就是为了处理客户端的连接
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)
# 上面建立的这个套接字作为被监听的对象，用来接收来自于客户端的连接

# 接下来应该关注读事件，因为和用户端连接这件事情，不是 server 能决定的
rlist = [s]  # 用于等待处理连接
wlist = []
xlist = []

# 循环监控IO
# 循环监控就可以不断的连接多个客户端，因为每次循环都会先查一下 rs 列表里的 s ，看是否有新的连接
while True:
    rs, ws, xs = select(rlist, wlist, rlist)

    # 遍历返回值列表，处理就绪的IO
    for r in rs:  # 此时代表 s 就绪，代表还有客户端想要和服务端连接
        if r is s:
            c, addr = r.accept() # accept 这句就是用来处理客户端的连接的，返回的 c 是用来和客户端进行交互的新的套接字
            print("Connected from", addr)
            rlist.append(c)  # 增加新的IO关注
        else:  # else 的情况就应该是 c 就绪，代表客户端给我服务端消息
            data = r.recv(1024).decode()
            # 客户端退出了
            if not data:
                rlist.remove(r)  # 取消对客户端的关注
                r.close()
                continue
            print(data)
            # r.send(b'ok') # 这个是主动的呀，可以放在 ws 里面
            wlist.append(r) # 把给服务端发消息的客户端放在写列表里面

    for w in ws:
        w.send(b'ok')
        wlist.remove(w) # 每一次发完消息就应该直接移除，要不然就没完没了了

    for x in xs:
        pass
