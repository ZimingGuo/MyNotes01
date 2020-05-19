# author: Ziming Guo
# time: 2020/2/11
"""
    demo03：
        函数内存图
"""

# 在方法区中存储函数代码,不执行函数体
def fun01(a):
    a = 100

num01 = 1
# 因为调用函数，所以开辟一块内存空间，叫做栈帧
# 用于存储在函数内部定义的变量(包含参数).
fun01(num01) # 这句话就是要把 num01 给 a
             # 也就是让 a 指向 num01 所指向的数据
             # 这句话就是：在内存里开辟了一块栈帧，告诉栈帧 a = num01
# 函数执行完毕后，栈帧立即释放(其中定义的变量也会销毁，即 a 也没了).
#   也就是栈帧立即销毁了
#   栈帧立即销毁了，里面的变量都销毁了
#   但是变量所指向的对象是否销毁了，不知道（要看这个数据的引用级数）
print(num01)#1



def fun02(a):
    # 改变的是传入的可变对象
    a[0] = 100

list01 = [1]
fun02(list01)
print(list01[0])# 100


def fun03(a):
    # 改变的是fun03栈帧中变量a的指向
    a = 100   # 如果要是这样写的话，改变的就不是列表里的元素了
              #     而是 a 不再指向原来那个列表了，指向了一个新的数值
              #     可变类型 可以改变，而不是一定会改变
list01 = [1]
fun03(list01)
print(list01[0])# 1


def fun04(a):
    a[1] = [200]

list01 = [1,[2,3]]
fun04(list01) # 此时调用函数了，所以开辟了栈帧区域
print(list01[1])# [200]


