# author: Ziming Guo
# time: 2020/3/3
"""
    在不改变原有功能(fun01 fun02)调用与定义情况下，
    为其增加新功能(打印函数执行时间).
"""

import time


def get_execute_time(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        re = func(*args, **kwargs)
        time_end = time.time()
        time_sub = time_end - time_start
        print("fun01函数执行时间为：%.3f" % time_sub)
        return re

    return wrapper


@get_execute_time
def fun01():
    time.sleep(2)
    print("执行完毕咯！")


@get_execute_time
def fun02(a):
    time.sleep(1)
    print("fun02执行完毕，参数是", a)


fun01()
fun02(100)

# 通过计算程序执行时间这个练习
#   明白：装饰器函数不是只能在就函数执行前进行操作，在程序执行完之后也是可以进行操作的
#   比如获取时间啥的。重要的是知道装饰器函数的运行原理，这样就知道原函数是在哪里开始执行
#   也可以知道函数是在哪里结束执行的，就可以根据自己需求加东西。
