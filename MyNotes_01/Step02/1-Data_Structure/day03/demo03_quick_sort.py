# author: Ziming Guo
# time: 2020/3/13
"""
    demo03:
        实现快速排序（快排）
"""
# 一轮交换
def sub_sort(l, low, high):
    x = l[low]  # 选定基准
    while low < high: # 只要是二者没有碰上，就一直循环
        # 后面的数向前甩
        while l[high] > x and high > low: # 只要是 high 索引的数大于基准数
            high -= 1  # high 向前（左）走一个；只要是大就往前挪一个，看下一个数
        l[low] = l[high]  # 将比基准小的数放到 low 的位置，但是此时 high 位置就空出来了，然后就执行下面的这些语句
        # 前面的数往后甩
        while l[low] <= x and low < high:
            low += 1
        l[high] = l[low]  # 将比基准大的数放到后面
    l[low] = x  # 将基准数插入回去
    return low
# 整体的思想就是：前面的数大于基准，就往后放
# 后面的数小于基准，就往前放

# 快速排序
def quick(l, low, high):
    """
    :param l: 要被快速排序的列表
    :param low: 第一个元素索引
    :param high: 最后一个元素的索引
    """
    if low < high:  # 如果low < high就做一个排序
        key = sub_sort(l, low, high)
        quick(l, low, key - 1)
        quick(l, key + 1, high)


l = [4, 9, 3, 1, 2, 5, 8, 4]
# bubble(l)
quick(l, 0, len(l) - 1)
print(l)  # 有序
