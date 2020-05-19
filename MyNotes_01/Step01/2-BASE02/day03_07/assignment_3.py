# author: Ziming Guo
# time: 2020/2/10
'''
    作业3：
     定义在控制台中打印二维列表的函数
        [
            [1,2,3,44],
            [4,5,5,5,65,6,87]
            [7,5]
        ]

        1 2 3 44
        4 5 5 5 65 6 87
        7 5
'''
list01 = \
    [
        [1, 2, 3, 44],
        [4, 5, 5, 5, 65, 6, 87],
        [7, 5]
    ]


def print_2_dimension_list(list):
    """
    打印二维字符串
    :param list: 所要打印的二维字符串
    :return:
    """
    for item in list:
        for i in range(len(item)):
            if i == len(item) - 1:
                print(item[i])
                break  # 或者把这两句换成 print() 这也可以打出来一个换行
                       # 因为 print 函数自带换行的功能
            print(item[i], end=" ")


print_2_dimension_list(list01)
