# author: Ziming Guo
# time: 2020/2/29
'''
    作业3：
    定义敌人类(姓名,攻击力,防御力,血量)
   创建敌人列表,使用list_helper实现下列功能.
   (1) 查找姓名是"灭霸"的敌人
   (2) 查找攻击力大于10的所有敌人
   (3) 查找活的敌人数量
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


# 生成函数的方法：
def condition_mieba(item):
    return item.name == "灭霸"


def condition_atk_above_10(item):
    return item.atk > 10


def condition_alive(item):
    return item.hp > 0


print(ListHelper.find_single_condition(list_enemy, condition_mieba))

for item in ListHelper.find_all(list_enemy, condition_atk_above_10):
    print(item)

print(ListHelper.find_count_number(list_enemy, condition_alive))

print("--------------------------------------------------------------")
# lambda 的方法：
print(ListHelper.find_single_condition(list_enemy, lambda element: element.name == "灭霸"))

for item in ListHelper.find_all(list_enemy, lambda element: element.atk > 10):
    print(item)

print(ListHelper.find_count_number(list_enemy, lambda element: element.hp > 0))
