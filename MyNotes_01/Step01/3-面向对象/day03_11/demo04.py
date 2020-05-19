# author: Ziming Guo
# time: 2020/2/17
"""
    demo04：
    封装设计思想
        需求：老张开车去东北
"""


class Person:
    def __init__(self, name):
        self.name = name # 程序运行到这里，像给变量写东西，但是被拦截了
                         #   所以会进入到拦截的那个方法，通过方法来写入

    @property # 创建方法，用于以后读取变量
    def name(self):
        return self.__name

    @name.setter # 创建方法，用于以后写入 / 修改变量
    def name(self, value):
        self.__name = value # 这个方法的作用就是：把 value 传给 __name

    def go_to(self, str_postion, type): # 创建类方法，作用是直接打印
        """
            去
        :param str_postion: 位置
        :param type: 方式　
        """
        print(self.name, "去", str_postion)
        type.run(str_postion)


class Car: # 又创建了一个类
    def run(self, str_position): # 创建了一个类方法
        """
            行驶
        :param str_position: 位置　
        """
        print("汽车行驶到:", str_position)


lz = Person("老张") # 创建了一个第一个类的对象
car = Car() # 创建了一个第二个类的对象，但是不会执行什么操作，只是创建了一个对象
# 老张开车去东北
lz.go_to("东北", car) # 调用了第一个类的方法，这个方法里要两个参数
                     #      其中，第一个类的方法里面又调用了第二个类的方法
