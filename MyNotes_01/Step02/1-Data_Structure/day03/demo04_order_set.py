# author: Ziming Guo
# time: 2020/3/14
'''
    三种排序集合的汇总：冒泡；选择；插入
'''


# 冒泡排序：双层循环
def bubble(list_):
    for m in range(0, len(list_) - 1):
        for n in range(m + 1, len(list_)):  # 注意这个地方一定是从 m 开始的
            if list_[m] > list_[n]:
                list_[m], list_[n] = list_[n], list_[m]


# 选择排序
def seq_ord(list_target):
    """
        把一个列表用选择排序的方式从小到大排列
        思想：
         1） 找剩下的元素里最小的元素
         2） 把这个元素和最前面的那个元素交换
    :param list_target: 要排列的列表
    """
    for m in range(0, len(list_target) - 1):
        dict_min = {}
        dict_min["val"] = list_target[m]
        dict_min["ind"] = m
        for i in range(m + 1, len(list_target)):
            if list_target[i] < dict_min["val"]:
                dict_min["val"] = list_target[i]  # 找到了最小的元素,存数据
                dict_min["ind"] = i  # 找到了最小元素,存索引值

        list_target[m], list_target[dict_min["ind"]] = dict_min["val"], list_target[m]


# 插入排序
def insert_ord(list_target):
    """
        思想：
        # 1 按顺序拿出来一个元素，和前面的进行比较
        # 2 当比到一个比他小的元素后，就插在他的前面一个位置
        # 注意：比较是和前面的元素进行比较
        # 注意：是插入而不是交换（insert）
    :param list_target: 要进行排序的列表
    """
    for m in range(1, len(list_target)):
        for n in range(m - 1, -1, -1):
            if list_target[n] < list_target[m]:
                list_target.insert(n + 1, list_target[m])
                del list_target[m + 1]
                break
            elif n == 0:
                list_target.insert(0, list_target[m])
                del list_target[m + 1]
