# author: Ziming Guo
# time: 2020/3/2
'''
    作业3：
    在list_helper.py中新增以下功能：
        (1)获取最小值
        (2)降序排列
        (3)根据指定条件删除元素
           （注意曾经的经验:倒着删除）
           案例:在敌人列表中，删除所有死人.
           案例:在敌人列表中，攻击力小于50的所有敌人.
           案例:在敌人列表中，防御力大于100的所有敌人.
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
    Enemy("霸天虎", 19, 13, 85),
    Enemy("灭霸", 30, 15, 69),
    Enemy("鲨鱼辣椒", 8, 6, 77),
    Enemy("大坏人", 6, 2, 0),
    Enemy("成昆", 55, 5, 0)
]

from common_my.list_helper_2 import *


# （1）

def smaller_condition(item):
    return item.atk


print(ListHelper.get_min(list_enemy, smaller_condition))

print(ListHelper.get_min(list_enemy, lambda item: item.atk))

# 注意：定义的新的条件函数的作用，只是，把要比较 or 提取的变量提取出来，不用做别的

print("------------------------------------------------")

# (2)
for item in ListHelper.down_order_ranking(list_enemy, lambda item: item.atk):
    print(item)

print("------------------------------------------------")


# (3)

# def delete_condition_01(item):
#     return item.atk == 0
#
#
# for item in ListHelper.delete_element(list_enemy, delete_condition_01):
#     print(item)

print("------------------------------------------------")


# def delete_condition_02(item):
#     return item.atk < 50
#
#
# for item in ListHelper.delete_element(list_enemy, delete_condition_02):
#     print(item)

print("------------------------------------------------")


def delete_condition_03(item):
    return item.atk > 100


for item in ListHelper.delete_element(list_enemy, delete_condition_03):
    print(item)
