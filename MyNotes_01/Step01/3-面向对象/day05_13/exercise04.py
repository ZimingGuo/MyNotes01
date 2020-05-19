# author: Ziming Guo
# time: 2020/2/21
"""
    练习4：
    定义图形管理器类
        1. 管理所有图形
        2. 提供计算所有图形总面积的方法

    具体图形:
        圆形(pi × r ** 2)
        矩形(长*宽)
        ...

    测试：
        创建1个圆形对象，1个矩形对象，添加到图形管理器中.
        调用图形管理器的计算面积方法，输出结果。

    要求：增加新图形，不修改图形管理器的代码.
    体会：面向对象三大特征：
            封装/继承/多态
         面向对象设计原则：
            开闭/单一/倒置

"""


class IconController:
    def __init__(self, name):
        self.__name = name


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.name = value

    def start_to_calculate(self, object):
        if not isinstance(object, Icon):
            print("此图形不在计算范围")
            raise ValueError("不是Damageable的子类")
        area = object.calculate()
        print(self.name, "的面积是：", area)

    # @property
    # def value01(self):
    #     return self.__value01
    #
    # @value01.setter
    # def value01(self, value):
    #     self.__value01 = value
    #     return self.__value01
    #
    # @property
    # def value02(self):
    #     return self.__value02
    #
    # @value01.setter
    # def value02(self, value):
    #     self.__value02 = value
    #     return self.__value02


class Icon:
    def calculate(self):
        raise NotImplementedError()

 # ----------------------- 架构师工作 over ------------------------------
class Circle(Icon):
    def calculate(self):
        r = int(input("请输入半径r:"))
        # 这样写不太好的原因是：calculate 这个方法的作用就是计算面积，而不是获取参数
        # 应该在创建对象的时候就已经带有参数了
        # 具体的好的写法，见 edited 版本

        pi = 3.1415926
        area = pi * r ** 2
        return area


class Rectangle(Icon):
    def calculate(self):
        a = int(input("请输入边长a:"))
        b = int(input("请输入边长b:"))
        # 这样写不太好的原因是：calculate 这个方法的作用就是计算面积，而不是获取参数
        # 应该在创建对象的时候就已经带有参数了
        # 具体的好的写法，见 edited 版本

        area = a * b
        return area


ic01 = IconController("圆")
ic02 = IconController("矩形")
c01 = Circle()
r01 = Rectangle()

ic01.start_to_calculate(c01)
ic02.start_to_calculate(r01)
