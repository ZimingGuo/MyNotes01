# author: Ziming Guo
# time: 2020/2/15
'''
    练习3：
        定义对象计数器、
        定义老婆类，创建3个老婆对象
        可以通过类变量记录老婆对象个数
        可以通过类方法打印老婆对象个数
        要求：画出内存图
'''


class Wife:
    count = 0  # 定义了一个类变量

    # 每次创建一个对象都会调用一次 __init__ 方法
    # 随意计数器技术应该在 __init__ 方法里面
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        Wife.count += 1 # 在实例方法里面可以访问 / 操作类成员
                        # 而 在类方法里面不可以访问实例变量

    @classmethod  # 创建了一个类方法
    def print_number(cls):
        print("这是第%d次打印老婆对象" % (Wife.count))


# 建立一次对象就会调用一次 __init__ 方法，因此 count 就会+1

w01 = Wife(1, 2, 3)  # 创建了一个对象
Wife.print_number()  # 调用了一次类方法

w02 = Wife(4, 5, 6)  # 又创建了一个对象
Wife.print_number()  # 又调用了一次类方法

w03 = Wife(7, 8, 9)  # 又创建了一个对象
Wife.print_number()  # 又调用了一次类方法
