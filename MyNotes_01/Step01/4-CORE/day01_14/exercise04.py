# author: Ziming Guo
# time: 2020/2/22
"""
    练习4：
    导入方式
    练习1：
        将day11/day10_exercise/exercise01.py中的
        Vector2和DoubleListHelper定义到
          double_list_helper.py模块中.
    练习2:
        在exercise03.py模块中，实现
        (1)在二维列表中，获取13位置，向左，3个元素

        (2)在二维列表中，获取22位置，向上，2个元素

        (3)在二维列表中，获取03位置，向下，2个元素
    要求：使用三种导入方式
    体会：哪一种更合适。
"""

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]

# 第一种方式
# import double_list_helper as dlh
#

#
# point01 = dlh.GetVectorHelper.get_elements(list01, dlh.Vector(1, 3), "left", 2)
# point02 = dlh.GetVectorHelper.get_elements(list01, dlh.Vector(2, 2), "up", 2)
# point03 = dlh.GetVectorHelper.get_elements(list01, dlh.Vector(0, 3), "down", 2)
# print(point01)
# print(point02)
# print(point03)


# 第二种导入方式
# from double_list_helper import GetVectorHelper
# from double_list_helper import Vector
#
# point01 = GetVectorHelper.get_elements(list01, Vector(1, 3), "left", 2)

# 第三种导入方式
from double_list_helper import *

point01 = GetVectorHelper.get_elements(list01, Vector(1, 3), "left", 2)
