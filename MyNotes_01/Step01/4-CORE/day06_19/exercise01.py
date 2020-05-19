# author: Ziming Guo
# time: 2020/3/3
"""
    练习：在不该变原有功能(存取钱)的定义与调用情况下.
         增加验证账号的功能．
"""


def verify_func(func):
    def wrapper(*args, **kwargs):
        print("请先验证账号！")
        return func(*args, **kwargs)

    return wrapper  # 此处不应该有括号，因为有括号就代表执行方法了，此处不是让他执行


@verify_func
def deposit(money):
    print("存%d钱咯！" % money)


@verify_func
def withdraw(log_in, password):
    print("取钱咯！", log_in, password)


deposit(9999) # 执行的时候被装饰器拦截了

withdraw("haha", 12345)
