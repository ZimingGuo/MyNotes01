# author: Ziming Guo
# time: 2020/2/10
'''
    练习9:
    将下列代码，定义到函数中，再调用一次.
    for r in range(3):  # 0    1     2
        # 内层循环控制列　
        for c in range(4):  # 0123  0123  0123
            print("*", end=" ")
        print()
'''
def draw_rectangle(row,column,icon): # 程序执行到这里就不会执行了
                                # 因为是函数的定义，而不是使用函数
                                # 只有调用的时候才会执行里面的代码
    """
    画一个用星号组成的矩形
    :param row: 表示行 int
    :param column: 表示列 int
    :param icon:表示所画的矩形里面填充的图形
    :return:
    """
    for r in range(row):
        for c in range(column):
            print(icon, end=" ")
        print()

draw_rectangle(5,5,"5")
