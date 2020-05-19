# author: Ziming Guo
# time: 2020/2/28
"""
    列表助手模块
"""


# 这就相当于写了一个类
# 这个类里面都是静态方法，以后直接调用这个类就行


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素,生成器类型.
        """
        for item in list_target:
            if func_condition(item):
                yield item
                # 类中的方法应该属于实例方法
                # 调用实例方法的时候必须要一个对象来调用，因为往往实例方法需要类里的数据
                # 但是现在不用类里面的数据，也就不是必须要对象来调用这个方法了
                # 所以做成一个静态方法，为后续调用

    # 这也就体现了整体面向对象，内部面向函数(函数式编程)

    @staticmethod
    def find_single_condition(list_target, func_condition):
        """
            通用的查找某个条件的单个元素的方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
        :return: 需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def find_count_number(list_target, func_condition):
        """
            通用的查找某个条件的元素的个数的方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
        :return: 满足条件的元素个数
        """
        number = 0
        for item in list_target:
            if func_condition(item):
                number += 1
        return number

    @staticmethod
    def whether_have_the_element(list_target, func_condition):
        """
            查看列表里是否具有符合条件的元素，返回的是 bool 形式
        :param list_target: 待查看列表
        :param func_condition: 需要查找的条件,函数类型
        :return: True / False
        """
        for item in list_target:
            if func_condition(item):
                return True
        return False
