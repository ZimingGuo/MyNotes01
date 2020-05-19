# author: Ziming Guo
# time: 2020/2/24
"""
    练习4:
        敌人类(攻击力0--100)
        抛出异常的信息：消息/错误行/攻击力/错误编号
"""


class AtkError(Exception):
    def __init__(self, error_message, error_line, atk_value, number):
        self.error_message = error_message
        self.error_line = error_line
        self.atk_value = atk_value
        self.number = number


class Enemy:
    def __init__(self, atk):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 < value < 100:
            self.__atk = value
        else:
            raise AtkError("atk数值错误", 27, value, 1001)


# a01 = Enemy(120)
# print(a01.atk)

try:
    a01 = Enemy(120)
except AtkError as atk_error:
    print(atk_error.error_message)
    print(atk_error.error_line)
    print(atk_error.atk_value)
    print(atk_error.number)
