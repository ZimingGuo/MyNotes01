# author: Ziming Guo
# time: 2020/2/10
'''
    练习8:
    矩阵转置  将二维列表的列，变成行，形成一个新列表.
      第一列变成第一行
      第二列变成第二行
      第三列变成第三行
'''
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# list03 = []
# for m in range(len(list01[0])):
#     list02 = []
#     list03.append(list02) # 这句话只是告诉程序：把list02放在list03里面
#                           # 而不是执行完这句话，才把list01加进去
#                           # 不是一个执行过程，所以上一句的 list02=[]对他影响不大
#     for i in range(len(list01)):
#         list02.append(list01[i][m])
# print(list03)

list03 = []
for m in range(len(list01[0])):

    list03.append([])     # 这句话只是告诉程序：把list02放在list03里面
                          # 而不是执行完这句话，才把list01加进去
                          # 不是一个执行过程，所以上一句的 list02=[]对他影响不大
    for i in range(len(list01)):
        list03[m].append(list01[i][m])
print(list03)

# 经验：
#  list.append()不是一个执行的操作，更像是一种状态，告诉程序把什么东西放在列表里
#  所以 append 语句所发挥的作用 和 它所放在程序中的位置没有很大关系
