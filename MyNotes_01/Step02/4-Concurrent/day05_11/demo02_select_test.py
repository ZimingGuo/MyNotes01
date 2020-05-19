# author: Ziming Guo
# time: 2020/4/4
'''
    demo02:
    select 函数示例
'''

from select import select
from socket import *

# 现在已经有一个 IO 对象了 s
s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(3)

f = open('log.txt', 'r+')

print("监控IO")
# 把想要关注的对象放在这三个列表当中
rs, ws, xs = select([s], [f], [], 3)  # 加上了最后的这个 3 秒的超时等待，就不会一直等待了

# 打印一下这三个返回值
print("rlist:", rs)  # 读事件是不能自己来决定的，必须要等待外界的条件达成才可以
print("wlist:", ws)  # socket 没有什么是需要主动去做的
print("xlist:", xs)
# 此时在等待监视的所有IO里面只要是有就绪的就不会阻塞了
