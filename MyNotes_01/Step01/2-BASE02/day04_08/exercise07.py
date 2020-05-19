# author: Ziming Guo
# time: 2020/2/11
'''
    练习7：
    定义 方阵转置 的函数
'''

def transpose_matrix(list_target):
    """
    方阵的转置
    :param list_target: 要转置的方阵，必须是方阵
    :return:
    """
    for a in range(len(list_target) - 1):
        for i in range(len(list_target) - 1 - a):
            list_target[a][i + 1], list_target[i + 1][a] = list_target[i + 1][a], list_target[a][i + 1]
    return list_target

list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
transpose_matrix(list01)
print(list01)
