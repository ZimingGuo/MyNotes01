# author: Ziming Guo
# time: 2020/2/17
"""
    练习4：
    请以面向对象的思想，描述下列场景:
        小明在招商银行取钱
"""


# 小明是个人，建立一个类，谁去干啥
# 去哪取钱，建立一个银行的类
# 去银行干啥，建立一个

class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def draw_money(self, who, value):
        self.money -= value
        who.money += value
        print(who.name, "去", self.name, "取", value)
        print(who.name, "还有", who.money)
        print(self.name, "还有", self.money)


xm = Person("小明", 200)
zsyh = Bank("招商银行", 1000)

zsyh.draw_money(xm, 100)

# m01.name="haha"
# print(m01.name)
