# author: Ziming Guo
# time: 2020/3/1
"""
    demo01:
    内置高阶函数

"""
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

# 1.filter:根据条件筛选可迭代对象中的元素，返回值为新可迭代对象
# 需求：获取所有死人
for item in ListHelper.find_all(list01, lambda item: item.hp == 0):
    print(item)

re = filter(lambda item: item.hp == 0, list01)

for item in re:
    print(item)

# 2.map:通用的筛选方法
# 需求：获取所有敌人的姓名
for item in ListHelper.filter_my_edited(list01, lambda item: item.name):
    print(item)
#
re = map(lambda item: item.name, list01)
for item in re:
    print(item)

# 3. max:获取最大值
# 需求：获取血量最大的敌人
print(ListHelper.get_max(list01, lambda item: item.hp))
print(max(list01, key=lambda item: item.hp))

# 4. min:获取最小值
# 略

# 5.
# 内部直接修改列表，使用时无需通过返回值获取数据
# ListHelper.order_by(list01,lambda item:item.atk)
# for item in list01:
#     print(item)

# 内部返回新列表，使用时必须获取返回值．
# re = sorted(list01, key=lambda item: item.atk)
# for item in re:
#     print(item)

# 支持降序排列
re = sorted(list01, key=lambda item: item.atk, reverse=True)
for item in re:
    print(item)