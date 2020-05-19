# author: Ziming Guo
# time: 2020/4/6
'''
    demo03:
    gevent 协程模块 示例
'''

import gevent

from gevent import monkey  # 首先倒入 monkey

monkey.patch_time()  # 在 time 导入之前，执行 patch_time
# 此处应注意，一定是要在 time 倒入之前执行 patch_time
# 之后，time 这个模块所对应的阻塞就会变成导致 gevent 跳转的阻塞

from time import sleep


# 写一个协程函数
def fun01(a, b):
    print("Running fun01...", a, b)
    sleep(2) # 此时就不用再用 gevent 去调用某个方法了
    print("fun01 again...")


def bar():
    print("Running bar...")
    sleep(3)
    print("Bar again...")


# 生成协程对象
# 这两句话就是让两个函数都变成协程了
f = gevent.spawn(fun01, 1, 2)
b = gevent.spawn(bar)

# 遇到了 joinall 就是要开始执行了
# 两个函数都开始执行
# 遇到了阻塞之后，会自动去查看是否有其他的过程可以去执行
gevent.joinall([f, b])  # 阻塞等待f,b两个协程执行完毕

# gevent.sleep(5)  # 只有这种阻塞才能够触发执行
# 只有满足了 gevent 的触发行为，他才能够被触发，然后执行
