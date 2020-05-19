# author: Ziming Guo
# time: 2020/2/25
"""
    练习5——edited：
    定义MyRange类，实现下列功能
    for item in range(10):
        print(item)
"""


class MyRange:
    def __init__(self, stop_value):
        self.stop_value = stop_value

    def __iter__(self):
        return MyRangeInterator(self.stop_value)


class MyRangeInterator:
    def __init__(self, end_value):
        self.__end_value = end_value
        self.__number = 0

    def __next__(self):
        if self.__number == self.__end_value:
            raise StopIteration
        temp = self.__number
        self.__number += 1
        return temp


# next 一次，计算一次，返回一次，所以不涉及数据太大 内存不够用的情况
# 这个例子就说明
#       在大数据时代，不能把数据全都摆出来
#       要写个算法，能退带出数据生成过程，调用一次使用一次
#       这是处理数据的方法，在数据时代
#       算一个给一个，给一个扔掉一个
for item in MyRange(10):  # 这里面的 MyRange 是创建了一个对象
    print(item)
