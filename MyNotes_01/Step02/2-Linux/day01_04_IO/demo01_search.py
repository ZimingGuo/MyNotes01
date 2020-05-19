# author: Ziming Guo
# time: 2020/3/14
'''
    demo01:二分查找
'''


def search(list_target, val):
    """

    :param list_target: 所要查找的列表
    :param val: 所要查找的数据值
    :return: 这个数据在数列中的索引位置
    """
    low, high = 0, len(list_target) - 1  # 查找范围的开始和结束索引位
    # 循环查找,每次去除一半
    while low <= high:
        mid = (low + high) // 2  # 中间数索引
        if list_target[mid] < val:
            low = mid + 1
        elif list_target[mid] > val:
            high = mid - 1
        else:
            return mid


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Key index:", search(l, 666))
