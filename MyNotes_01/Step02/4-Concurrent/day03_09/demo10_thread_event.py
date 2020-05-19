# author: Ziming Guo
# time: 2020/3/31
'''
    demo_event:
    event 线程互斥方法演示
'''

from threading import Thread, Event

s = None  # 用于通信，存口令
e = Event()  # 生成一个事件对象


def YZR():
    print("杨子荣前来拜山头\n")
    global s
    s = "天王盖地虎"
    e.set() # 操作完 s 才可以结束阻塞（操作完才能设置 e ）


t = Thread(target=YZR)

t.start()  # 开启了线程

print("说对口令，就是自己人")
e.wait() # 人为设置了一个阻塞等待
# 只有当操作完 s 之后，才能结束阻塞，继续执行

if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("ok")
else:
    print("kill you")

t.join()  # 回收线程

# 从运行的结果可以看出
# 有的时候就是 OK 有的时候就是 kill you
# 关键就是要看 修改全局变量 和 主线程(if判断) 哪个执行的快一点
# 两个线程互不相让
# " 谁先想占先机谁就赢，迟疑了就输了 "

# 阻塞实际上是控制了执行顺序
