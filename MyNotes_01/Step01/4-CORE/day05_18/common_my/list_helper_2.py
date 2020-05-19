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
    def whether_have_the_element_exist(list_target, func_condition):
        # 注意：如果不加  @staticmethod，def 会认为括号里面的参数是类里面的对象
        #      加上了静态方法就表示，我的参数是自己拿来的，而不是类里面原来定义的
        #      表示"我不要你给我的类和对象，我的参数是自己的，我不要你给我的参数啊"
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

    @staticmethod
    def get_total_sum(list_target, func_condition):
        """
            对列表里面的每个对象的某类元素进行加和
        :param list_target: 待操作列表
        :param func_condition: 需要查找的条件,函数类型
        :return: 和
        """
        total = 0
        for item in list_target:
            total = func_condition(item, total)
        return total

    @staticmethod
    def get_total_sum_edited(list_target, func_sum_object):
        """
            不同于上一个方法的是：这个方法直接返回的是元素，而没有在方法里面进行加和运算
        :param list_target: 待操作列表
        :param func_sum_object: 需要查找的条件,函数类型
        :return: 要加和的对象的数据
        """
        sum = 0
        for item in list_target:
            sum += func_sum_object(item)
        return sum

    @staticmethod
    def filter_my(list_target, func_filter):
        """
             对列表里面的每个对象的某类元素进行筛选
        :param list_target: 待操作列表
        :param func_filter: 想要筛选的数据，也就是条件，函数的形式
        :return: 筛选的数据组成的列表
        """
        list_obtain = []
        for item in list_target:
            list_obtain.append(func_filter(item))
        return list_obtain

    @staticmethod
    def filter_my_edited(list_target, func_filter_condition):
        """
            通用的筛选方法，用 yield 方法了，这是老师写的，我写的是上面的那个
            就是获得这个列表里面元素的某种数据 相当于 map
        :param list_target: 需要筛选的列表
        :param func_filter_condition: 需要筛选的处理逻辑,函数类型
                函数名(参数) --> int／str/元组/其他类型的对象
        :return: 生成器,一定要注意，返回出来的是一个生成器，出来之后要用 for 循环才能顺利操作
         """
        for item in list_target:
            yield func_filter_condition(item)

    @staticmethod
    def get_max(list_target, func_condition):
        """
            通用的选取列表里的对象的某个数据的最大值；func_condition 要三个参数
        :param list_target: 待处理列表
        :param func_condition: 需要挑选最大值的条件，即 找什么数据的最大值
        :return: 条件
        """
        bigger = list_target[0]
        for i in range(1, len(list_target)):
            if func_condition(bigger, i, list_target):
                bigger = list_target[i]
        return bigger

    @staticmethod
    def get_max_edited(list_target, func_condition):
        """
            上一个找最大条件的升级版 ；func_condition 要一个参数
        :param list_target:
        :param func_condition: 挑选最大值的条件，即 要找什么数据的最小值
        :return: 最大值的那个元素
        """
        bigger = list_target[0]
        for i in range(1, len(list_target)):
            if func_condition(bigger) < func_condition(list_target[i]):
                bigger = list_target[i]
        return bigger

    @staticmethod
    def get_min(list_target, func_condition):
        """
            通用的找列表里面某个数据最小的元素
        :param list_target: 待操作的列表
        :param func_condition: 挑选最小值的条件，即 要找什么数据的最小值
        :return: 最小值的那个元素
        """
        smaller = list_target[0]
        for i in range(1, len(list_target)):
            if func_condition(smaller) > func_condition(list_target[i]):
                smaller = list_target[i]
        return smaller

    @staticmethod
    def up_order_ranking(list_target, func_condition):
        """
            按照某一类数据升序的规则排列一个列表里的元素
        :param list_target: 待操作列表
        :param func_condition: 升序排列所依照的数据类型,即 需要比较的数据
        :return: 返回的列表就是升序排列之后的列表
        """
        for a in range(0, len(list_target) - 1):
            for b in range(a + 1, len(list_target)):  # 这个地方是 a+1 一定记住，b 是要和 a 的后一个元素进行比较的，而不是永远从
                if func_condition(list_target[a]) > func_condition(list_target[b]):
                    list_target[a], list_target[b] = list_target[b], list_target[a]
        return list_target

    @staticmethod
    def down_order_ranking(list_target, func_condition):
        """
            按照某一类数据升序的规则排列一个列表里的元素
        :param list_target: 待操作列表
        :param func_condition: 升序排列所依照的数据类型,即 需要比较的数据
        :return: 返回的列表就是升序排列之后的列表
        """
        for a in range(0, len(list_target) - 1):
            for b in range(a + 1, len(list_target)):  # 这个地方是 a+1 一定记住，b 是要和 a 的后一个元素进行比较的，而不是永远从
                if func_condition(list_target[a]) < func_condition(list_target[b]):
                    list_target[a], list_target[b] = list_target[b], list_target[a]
        return list_target

    @staticmethod
    def delete_element(list_target, func_condition):
        """
            通用的删除列表中某个元素的方法，根据某个数据的条件删除
        :param list_target: 待操作列表
        :param func_condition: 用来表示条件的函数，直接点类里面想要筛选的数据就可
        :return: 删除某类元素之后的列表
        """
        for i in range(len(list_target) - 1, -1, -1):
            if func_condition(list_target[i]):
                list_target.remove(list_target[i])
        return list_target

    # 做练习的时候的 experience :
    #   在写 func_condition 的时候一定要返回的是对象的一个数据
    #   然后在调用这个函数的时候，直接处理 or 判断的就是这个数据
    #   说白了就是要尽量保证：lambda 一个函数之后，函数执行完直接就有答案
