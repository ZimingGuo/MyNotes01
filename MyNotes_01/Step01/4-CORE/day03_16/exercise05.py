# author: Ziming Guo
# time: 2020/2/25
"""
    练习5：
    定义MyRange类，实现下列功能
    for item in range(10):
        print(item)
"""


class MyRange:
    def __init__(self, stop_value):
        self.stop_value = stop_value


class RangeManager:
    def __init__(self):
        self.__list_range = []

    def add_to_range(self, value02):
        self.__list_range.append(value02)

    def __iter__(self):
        return RangeInterator(self.__list_range)


class RangeInterator:
    def __init__(self, list):
        self.list = list
        self.index = 0

    def __next__(self):
        if self.index > len(self.list) - 1:
            raise StopIteration
        temp = self.list[self.index]
        self.index += 1
        return temp


i = 0
manager = RangeManager()  # 创建一个对象
while i < 10:
    manager.add_to_range(i)
    i += 1

r01 = manager.__iter__()
while True:
    try:
        item = r01.__next__()
        print(item)
    except StopIteration:
        break
