# author: Ziming Guo
# time: 2020/2/25
'''
    练习3：
    推导图形管理器的迭代器
'''


class Graphic:
    pass


class GraphicManager:
    """
        图形管理器
    """

    def __init__(self):
        self.__list_graphic = []

    def add_graphic(self, graphic):
        self.__list_graphic.append(graphic)

    def __iter__(self):
        return GraphicInterator(self.__list_graphic)


class GraphicInterator:
    """
        图形迭代器
    """

    def __init__(self, outside_list):
        self.__outside_list = outside_list
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__outside_list) - 1:
            raise StopIteration
        result = self.__outside_list[self.__index]
        self.__index += 1
        return result


manager = GraphicManager()
manager.add_graphic(Graphic())  # 在 GraphicManager 类里面添加 Graphic 类，添加进列表
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())

# for item in manager:
#     print(item)
# 这两句其实可以不写的，因为这两句是在跨过了原理，直接使用 for 的功能

# 下面这句才是应用原理实现功能
a = manager.__iter__() # 这句话就相当于给 a 返回来一个 GraphicInterator 的类
# 就是说我现在需要做一个东西，这个都关系可以调用 __iter__ 方法，准备迭代
# 调用完 __iter__ 方法之后返回的这个东西，又可以再调用 __next__ 方法进行依次获取元素 ®

while True:
    try:
        item = a.__next__()
        print(item)
    except StopIteration:
        break
