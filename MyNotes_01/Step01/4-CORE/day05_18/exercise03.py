# author: Ziming Guo
# time: 2020/3/1
'''
    练习1:
        先用内置高阶函数做，再用自己创建的方法实现。
        1. ([1,1,1],[2,2],[3,3,3,3])
           获取元组中，长度最大的列表.
        2. 根据敌人列表，获取所有敌人的姓名与血量与攻击力.
        3. 在敌人列表中，获取攻击力大于100的所有活人.
        4. 根据防御力对敌人列表进行降序排列.
'''

from common_my.list_helper_2 import *


class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.hp, self.atk, self.defense)


list01 = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]

tuple_list = ([1, 1, 1], [2, 2], [3, 3, 3, 3])

'''
第一道题：获取元组中，长度最大的列表
'''


# 内置函数：
# 获取每个列表长度
def get_length(tuple_target):
    length_value = []
    for item in tuple_target:
        length_value.append(len(item))
    return length_value


# 通过 max 函数求得最大值
re01 = max(get_length(tuple_list), key=lambda item: item)

# 心里要清楚，这个 filter 方法就相当于自己在 ListHelper 里面的 filter_my 静态方法
for element in filter(lambda item: len(item) == re01, tuple_list):
    print(element)

# 上面的这两种方式都是先定义一个计算长度的函数，其实用 max 内置函数也可以直接求出来元素长度
print(max(tuple_list, key=lambda item: len(item)))

# for element01 in map(lambda item: len(item) == 4, tuple_list):  # 这样写不行，因为这样返回的是一个装满了 True 和 False 的生成器
#     print(element01)

print("--------------------------------------------------------------")

# 自己的创建的静态方法：
re02 = ListHelper.get_max_edited(get_length(tuple_list), lambda item: item)

print(ListHelper.find_single_condition(tuple_list, lambda item: len(item) == re02))

print("--------------------------------------------------------------")

'''
第二道题：根据敌人列表，获取所有敌人的姓名与血量与攻击力
'''
# 内置函数：
for item in map(lambda item: (item.hp, item.atk), list01):
    print(item)

print("--------------------------------------------------------------")

# 自己创建的常用静态方法：
for item in ListHelper.filter_my_edited(list01, lambda item: (item.hp, item.atk)):
    print(item)

print("--------------------------------------------------------------")

"""
第三道题：在敌人列表中，获取攻击力大于100的所有活人 
"""
# 内置高阶函数：
for item in filter(lambda item: item.atk > 100 and item.hp > 0, list01):
    print(item)

print("--------------------------------------------------------------")

# 自己创建的常用静态方法：
for item in ListHelper.find_all(list01, lambda item: item.atk > 100 and item.hp > 0):
    print(item)

print("--------------------------------------------------------------")

"""
第四道题：根据防御力对敌人列表进行降序排列 
"""
# 内置高阶函数：
for item in sorted(list01, key=lambda item: item.atk, reverse=False):
    print(item)

print("--------------------------------------------------------------")

# 自己创建的常用静态方法：
for item in ListHelper.down_order_ranking(list01, lambda item: item.atk):
    print(item)
