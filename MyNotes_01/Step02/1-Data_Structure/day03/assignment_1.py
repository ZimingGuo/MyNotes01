# author: Ziming Guo
# time: 2020/3/13
'''
选择排序 & 插入排序
'''
# 选择排序


list01 = [3, 5, 2, 6, 8, 3, 4, 1, 4, 9]
list02 = [3, 5, 2, 6, 8, 3, 4, 1, 1, 1, 17, 7, 9, 4, 9]


# 1 找剩下的元素里最小的元素
# 2 把这个元素和最前面的那个元素交换
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
# 老师的方法是用 min 来存储最小值的索引值，然后传递数据的时候用再用索引值调取数据
# 这样就不用字典来储存数据和索引值了

# 测试代码
# seq_ord(list01)
# print(list01)
# experience：我发现选择排序方法都用到了两两交换的思想，因此就需要存储元素的索引值
#       那就自然会用到字典的形式

# 插入排序
# 1 按顺序拿出来一个元素，和前面的进行比较
# 2 当比到一个比他小的元素后，就插在他的前面一个位置
# 注意：比较是和前面的元素进行比较
# 注意：是插入而不是交换（insert）


def insert_ord(list_target):
    for m in range(1, len(list_target)):
        for n in range(m - 1, -1, -1):
            if list_target[n] < list_target[m]:
                list_target.insert(n + 1, list_target[m])
                del list_target[m + 1]
                break
            elif n == 0:
                list_target.insert(0, list_target[m])
                del list_target[m + 1]


insert_ord(list02)
print(list02)
