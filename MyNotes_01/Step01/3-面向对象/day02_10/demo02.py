# author: Ziming Guo
# time: 2020/2/15
"""
    demo02：
    类成员
    练习:exercise03.py
"""


class ICBC:
    """
        demo02：
        工商银行
    """
    # 表示总行的钱
    total_money = 1000000 # 这不是对象的数据，这是类的数据

    # 因为类方法没有对象地址self，所以不能访问实例成员
    @classmethod
    def print_total_money(cls):
        # print(id(cls),id(ICBC))
        print("总行还剩%d钱" % ICBC.total_money)

    def __init__(self, name, money): # 这些才是对象的数据
        self.name = name
        self.money = money
        # 表示从总行中扣除当前支行使用的金额
        ICBC.total_money -= money

i01 = ICBC("广渠门支行", 100000)
ICBC.print_total_money()
i02 = ICBC("陶然亭支行", 100000)
# print("总行还剩%d钱" % ICBC.total_money)

# 通过类名访问类方法，会将类名传入类方法.
ICBC.print_total_money()