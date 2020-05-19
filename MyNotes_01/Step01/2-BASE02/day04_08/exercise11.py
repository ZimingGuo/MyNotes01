# author: Ziming Guo
# time: 2020/2/11
'''
    作业:
    调用fun07
    参数的顺序
'''


# 位置形参 --> 星号元组形参 --> 命名关键字形参 --> 双星号字典形参

def fun07(a, b, *args, c, d, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)

    pass


fun07(1, 2, 3, 4, c=20, d=40, y=2, p=3, q=4)


# 又定义了一个函数
# 位置实参无限 + 关键字实参无限（这种参数的设置，就是传啥都行）
def fun01(*args, **kwargs):
    print(args)
    print(kwargs)


fun01(1, 2, 3, "oie", "uwm")
