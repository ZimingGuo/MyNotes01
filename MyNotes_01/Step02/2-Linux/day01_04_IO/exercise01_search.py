# author: Ziming Guo
# time: 2020/3/14
'''
    二分法在列表中查找数据
'''


def divide_search(list_target, val):
    """
        我这个不对，我这个只是分了两组数据，然后直接找，没有继续二分
    :param list_target: 要寻找的列表
    :param val: 要寻找的列表里面的数据
    :return: 索引值
    """
    count = len(list_target) // 2
    for i in range(count - 1):
        if list_target[i] == val:
            return i
    else:
        for j in range(count, len(list_target)):
            if list_target[j] == val:
                return j


list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(divide_search(list01, 3))
