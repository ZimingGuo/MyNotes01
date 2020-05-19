# author: Ziming Guo
# time: 2020/2/26
'''
    练习6:
        将迭代器版本的图形管理器改为yield实现.
        exercise03.py -->exercise06.py
'''


class Graphic:
    pass


class GraphicManager:
    """
        图形管理器
    """

    def __init__(self):
        self.__list_graphic = []
        self.__index = 0

    def add_graphic(self, graphic):
        self.__list_graphic.append(graphic)

    def __iter__(self):
        while self.__index < len(self.__list_graphic):
            yield self.__list_graphic[self.__index]
            self.__index += 1


# class GraphicInterator:
#     """
#         图形迭代器
#     """
#
#     def __init__(self, outside_list):
#         self.__outside_list = outside_list
#         self.__index = 0
#
#     def __next__(self):
#         if self.__index > len(self.__outside_list) - 1:
#             raise StopIteration
#         result = self.__outside_list[self.__index]
#         self.__index += 1
#         return result


manager = GraphicManager()
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())

a = manager.__iter__()

while True:
    try:
        item = a.__next__()
        print(item)
    except StopIteration:
        break
