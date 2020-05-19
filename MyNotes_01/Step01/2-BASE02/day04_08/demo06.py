# author: Ziming Guo
# time: 2020/2/11
"""
    demo06：
    函数参数
        形式参数
    练习:exercise09.py
    练习:exercise10.py
"""

# 1. 缺省(默认)形参:如果实参不提供，可以使用默认值.
#   如果实参没给全，就会用默认参数值代替
def fun01(a=None, b=0, c=0, d=0):
    print(a)
    print(b)
    print(c)
    print(d)

# 关键字实参 + 缺省形参:调用者可以随意传递参数.
# 如果只用缺形形参，那就会一直默认是前两个参数的值，只有用了关键字实参，才会定位
# fun01(b=2, c=3)


# 2. 位置形参
def fun02(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


# 3.星号元组形参: * 将所有实参 合并 为一个元组
# 作用：把所有形参合起来 让实参个数无限
def fun03(*args): # args 的意思就是很多个 argument 的意思
    print(args)
#   有了这个方法，以前对于元组那些操作方法(切片，索引 etc)都可以用了

# fun03()# ()
# fun03(1)# (1,)
# fun03(1,"2")# (1, '2')

# 4.命名关键字形参:在星号元组形参以后的位置形参
# 目的：要求实参必须使用关键字实参.
def fun04(a, *args, b):
    print(a)
    print(args)
    print(b)


fun04(1, b=2) # 用这种命名关键字形参必须有 a 和 b
              # 而中间的 *argu 不是必须的
fun04(1, 2, 3, 4, b=2)


def fun05(*, a, b):
    print(a)
    print(b)


fun05(a=1, b=2)


# 5. 双星号字典形参：**目的是将实参合并为字典.
#               实参可以传递数量无限的关键字实参.
#               最后打印出来的是个字典，把实参合并为字典
def fun06(**kwargs):
    print(kwargs)


fun06(a=1, b=2)


