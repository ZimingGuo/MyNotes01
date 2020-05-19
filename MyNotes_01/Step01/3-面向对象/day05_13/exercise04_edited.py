# author: Ziming Guo
# time: 2020/2/21
'''
    练习4_改进版
'''

class IconManager:
    def __init__(self):
        self.__icon_list = []

    # @property
    # def iconlist(self):
    #     return self.__icon_list

    def add_icon(self, icon):
        self.__icon_list.append(icon)

    def get_total_area(self):
        total_area = 0
        for item in self.__icon_list:
            if isinstance(item, Icon):
                total_area += item.calculate()
                # 此处体现了多态，调用的是  calculate 方法，但是实际上每一个 calculate 方法都是不一样的计算方式
        print(total_area)


class Icon:
    def calculate(self):
        raise NotImplementedError()


# ---------------------------------------------------------------

class Circle(Icon):
    def __init__(self, r):
        self.r = r

    def calculate(self):
        area = 3.14 * self.r ** 2
        return area


class Rectangle(Icon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate(self):
        area = self.length * self.width
        return area


i01 = IconManager()
c01 = Circle(2)
r01 = Rectangle(4, 5)

i01.add_icon(c01)
i01.get_total_area()
i01.add_icon(r01)
i01.get_total_area()
