# author: Ziming Guo
# time: 2020/3/1
'''
    练习2：
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

# 练习1：
'''
# 以下是最初的，没有提炼的代码
def get_total_hp(list_target):
    total_hp = 0
    for item in list_target:
        total_hp += item.hp
    return total_hp


def get_total_atk(list_target):
    total_atk = 0
    for item in list_target:
        total_atk += item.atk
    return total_atk


def get_total_defense(list_target):
    total_defense = 0
    for item in list_target:
        total_defense += item.defense
    return total_defense


print(get_total_hp(list_enemy))
print(get_total_atk(list_enemy))
print(get_total_defense(list_enemy))
'''


# 以下是封装继承多态之后的条件的代码
def condition_sum_hp(item, total_object):
    total_object += item.hp
    return total_object


def condition_sum_atk(item, total_object):
    total_object += item.atk
    return total_object


def condition_sum_defense(item, total_object):
    total_object += item.defense
    return total_object


print(ListHelper.get_total_sum(list_enemy, condition_sum_hp))
print(ListHelper.get_total_sum(list_enemy, condition_sum_atk))
print(ListHelper.get_total_sum(list_enemy, condition_sum_defense))

print("------------------------------------------------")

'''
    练习2:
    在list_helper.py中增加通用的筛选方法.
    案例1:获取敌人列表中所有敌人的名称.
    案例2:计算敌人列表中所有敌人的攻击力.
    案例3:计算敌人列表中所有敌人的名称和血量.
'''


# 以下为推导代码
def filer01(list_target):
    list01 = []
    for item in list_target:
        list_inter = []
        list_inter.append(item.name)
        list01.append(list_inter)
    return list01


def filer02(list_target):
    list02 = []
    for item in list_target:
        list_inter = []
        list_inter.append(item.atk)
        list02.append(list_inter)
    return list02


def filer03(list_target):
    list03 = []
    for item in list_target:
        list_inter = []
        list_inter.append(item.name)
        list_inter.append(item.hp)
        list03.append(list_inter)
    return list03


print(filer01(list_enemy))
print(filer02(list_enemy))
print(filer03(list_enemy))

print("------------------------------------------------")


# 以下为"封装""继承""多态"之后的代码：


def condition_filter_name(item):
    list_inter = []
    list_inter.append(item.name)
    return list_inter


def condition_filter_atk(item):
    list_inter = []
    list_inter.append(item.atk)
    return list_inter


def condition_filter_name_hp(item):
    list_inter = []
    list_inter.append(item.name)
    list_inter.append(item.hp)
    return list_inter


print(ListHelper.filter_my(list_enemy, condition_filter_name))
print(ListHelper.filter_my(list_enemy, condition_filter_atk))
print(ListHelper.filter_my(list_enemy, condition_filter_name_hp))

print("------------------------------------------------")

'''
    练习3:
    在list_helper.py中增加通用的获取最大值方法.
    案例1:获取敌人列表中攻击力最大的敌人.
    案例2:获取敌人列表中防御力最大的敌人.
    案例3:获取敌人列表中血量最高的敌人.
'''

# 以下为推导代码：

'''
def get_max_atk(list_target):
    bigger = list_target[0]
    for i in range(1, len(list_target)):
        if bigger.atk < list_target[i].atk:
            bigger = list_target[i]
    return bigger

print(get_max_atk(list_enemy))
'''


def condition_max_atk(object, number, list_inter):
    return object.atk < list_inter[number].atk


def condition_max_defense(object, number, list_inter):
    return object.defense < list_inter[number].defense


def condition_max_hp(object, number, list_inter):
    return object.hp < list_inter[number].hp


print(ListHelper.get_max(list_enemy, condition_max_atk))
print(ListHelper.get_max(list_enemy, condition_max_defense))
print(ListHelper.get_max(list_enemy, condition_max_hp))

print("------------------------------------------------")

# 用 lambda 的方式写
print(ListHelper.get_max(list_enemy, lambda object, number, list_inter: object.atk < list_inter[number].atk))
print(ListHelper.get_max(list_enemy, lambda object, number, list_inter: object.defense < list_inter[number].defense))
print(ListHelper.get_max(list_enemy, lambda object, number, list_inter: object.hp < list_inter[number].hp))

print("------------------------------------------------")

'''
    练习4:
    在list_helper.py中增加通用的升序排列方法.
    案例1:将敌人列表按照攻击力进行升序排列.
    案例2:将敌人列表按照防御力进行升序排列.
    案例3:将敌人列表按照血量进行升序排列.
'''


def condition_atk_up_ranking(item):
    return item.atk


def condition_defense_up_ranking(item):
    return item.defense


def condition_hp_up_ranking(item):
    return item.hp


for item in ListHelper.up_order_ranking(list_enemy, condition_atk_up_ranking):
    print(item)

print("------------------------------------------------")

for item in ListHelper.up_order_ranking(list_enemy, condition_defense_up_ranking):
    print(item)

print("------------------------------------------------")

for item in ListHelper.up_order_ranking(list_enemy, condition_hp_up_ranking):
    print(item)
