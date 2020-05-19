# author: Ziming Guo
# time: 2020/2/29
'''
    作业4：
    在list_helper中增加判断是否存在某个对象的方法.返回值:true/false
    案例1:判断敌人列表中是否存在"成昆"
    案例2:判断敌人列表中是否存在攻击力小于5或者防御力小于10的敌人.
    步骤:
    实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
    将不变的函数提取到list_helper.py中
    体会：函数式编程的思想("封装，继承，多态")
'''


class Enemy:
    def __init__(self, name, atk, defense, hp):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.hp = hp

    def __str__(self):
        return "名字是%s，攻击力是%d，防御力是%d，血量是%d" % (self.name, self.atk, self.defense, self.hp)
    # 再写一遍这个 __str__ 方法的作用：
    # 有了这个方法之后，再次打印 item 的时候就会按照这个方法里的返回值的形式来返回字符串了


list_enemy = [
    Enemy("威震天", 15, 10, 80),
    Enemy("霸天虎", 19, 9, 85),
    Enemy("灭霸", 30, 9, 69),
    Enemy("鲨鱼辣椒", 8, 6, 77),
    Enemy("大坏人", 6, 5, 0),
    Enemy("成昆", 55, 5, 0)
]

from common_my.list_helper_2 import *


def condition_name_ck(item):
    return item.name == "成昆"


def condition_atk_defnese(item):
    return item.atk < 5 or item.defense > 10


print(ListHelper.whether_have_the_element_exist(list_enemy, condition_name_ck))
print(ListHelper.whether_have_the_element_exist(list_enemy, condition_atk_defnese))
