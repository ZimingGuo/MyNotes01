# author: Ziming Guo
# time: 2020/3/14
'''
    用二分法实现列表中数据的寻找
'''
def search(list_target, val):
    low,high = 0, len(list_target) - 1 # 查找范围的开始和结束索引位
    # 循环查找,每次去除一半
    while low <= high:
        mid = (low + high) // 2  # 中间数索引
        if list_target[mid] < val:
            low = mid + 1
        elif list_target[mid] > val:
            high = mid - 1
        else:
            return mid
