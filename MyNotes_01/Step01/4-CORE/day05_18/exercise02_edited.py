# author: Ziming Guo
# time: 2020/3/1
'''
    练习2——edited：
                练习要求如下：
'''
'''
    练习１：
    在list_helper.py中增加通用的求和方法.
    案例1:计算敌人列表中所有敌人的总血量.
    案例2:计算敌人列表中所有敌人的总攻击力.
    案例3:计算敌人列表中所有敌人的总防御力.
    步骤：
    实现具体功能/提取变化/提取不变/组合
'''
'''
    练习4:
    在list_helper.py中增加通用的升序排列方法.
    案例1:将敌人列表按照攻击力进行升序排列.
    案例2:将敌人列表按照防御力进行升序排列.
    案例3:将敌人列表按照血量进行升序排列.
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


def sum_hp(item):
    return item.hp


def sum_atk(item):
    return item.atk


def sum_defense(item):
    return item.defense


print(ListHelper.get_total_sum_edited(list_enemy, sum_hp))
print(ListHelper.get_total_sum_edited(list_enemy, sum_atk))
print(ListHelper.get_total_sum_edited(list_enemy, sum_defense))

print("------------------------------------------------")

# lambda 形式

print(ListHelper.get_total_sum_edited(list_enemy, lambda item: item.hp))
print(ListHelper.get_total_sum_edited(list_enemy, lambda item: item.atk))
print(ListHelper.get_total_sum_edited(list_enemy, lambda item: item.defense))

print("------------------------------------------------")

'''
    练习2:
    在list_helper.py中增加通用的筛选方法.
    案例1:获取敌人列表中所有敌人的名称.
    案例2:计算敌人列表中所有敌人的攻击力.
    案例3:计算敌人列表中所有敌人的名称和血量.
'''
'''
# 可以看到，这种方法里面如果要筛选多个元素，就要用元组的方式来封装，因为按需分配而且不需要再做改变
def select01():
    result = []
    for item in list_enemy:
        result.append(item.name)
    return result

def select02():
    result = []
    for item in list_enemy:
        result.append(item.atk)
    return result

def select03():
    result = []
    for item in list_enemy:
        result.append((item.name,item.hp))
    return result
'''


def filter_name(item):
    return item.name


def filter_atk(item):
    return item.atk


def filter_name_hp(item):
    return (item.name, item.hp)


for item in ListHelper.filter_my_edited(list_enemy, filter_name):
    print(item)
for item in ListHelper.filter_my_edited(list_enemy, filter_atk):
    print(item)
for item in ListHelper.filter_my_edited(list_enemy, filter_name_hp):
    print(item)

print("------------------------------------------------")

# 用 lambda 的方法
for item in ListHelper.filter_my_edited(list_enemy, lambda item: item.name):
    print(item)
for item in ListHelper.filter_my_edited(list_enemy, lambda item: item.atk):
    print(item)
for item in ListHelper.filter_my_edited(list_enemy, lambda item: (item.name, item.hp)):
    print(item)

print("------------------------------------------------")

'''
    练习3:
    在list_helper.py中增加通用的获取最大值方法.
    案例1:获取敌人列表中攻击力最大的敌人.
    案例2:获取敌人列表中防御力最大的敌人.
    案例3:获取敌人列表中血量最高的敌人.
'''


def condition_max_atk(item):
    return item.atk


def condition_max_defense(item):
    return item.defense


def condition_max_hp(item):
    return item.hp


print(ListHelper.get_max_edited(list_enemy, condition_max_atk))
print(ListHelper.get_max_edited(list_enemy, condition_max_defense))
print(ListHelper.get_max_edited(list_enemy, condition_max_hp))
