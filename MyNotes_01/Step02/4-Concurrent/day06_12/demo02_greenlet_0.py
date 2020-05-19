# author: Ziming Guo
# time: 2020/4/6
'''
    demo02:
    协程行为
    用这个小示例体会一下什么是协程跳转，在两个函数之间进行有选择性的执行
'''

from greenlet import greenlet


def fun01():
    print("执行fun01")
    gr02.switch()
    print("结束fun01")
    gr02.switch()


def fun02():
    print("执行fun02")
    gr01.switch()
    print("结束fun02")


# 先将函数编程协程
gr01 = greenlet(fun01)
gr02 = greenlet(fun02)
# 将函数放进去之后，这两个对象就变成协程对象了

# 启动协程对象
gr01.switch()  # 表示选择执行哪个协程
