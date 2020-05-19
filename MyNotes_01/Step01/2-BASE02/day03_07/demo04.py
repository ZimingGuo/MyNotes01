# author: Ziming Guo
# time: 2020/2/9
'''
    demo04：
        for for
        不是为了画图形，而是看这种思想能够解决什么问题
'''

# print("*", end=" ")
# print("*", end=" ")
# # 这两句话的意思是，让这个 * 向右侧排列
# # end=" " 这句话决定的就是下一句话的内容排在哪里

# 外层循环控制行
for r in range(3):  # 0    1     2
    # 内层循环控制列　
    for c in range(4):  # 0123  0123  0123
        print("*", end=" ")
    print()

'''
        *#*#*#
        *#*#*#
        *#*#*#
        *#*#*#
'''
for r in range(4):  # 控制有几行（实际上控制打印几行）
    for c in range(6):  # 控制有几列（实际上控制每一行打印什么）
        if c % 2 == 0:
            print("*", end=" ")
        elif c % 2 == 1:
            print("#", end=" ")
    print()

'''
    外层4　　　　内层
    *              0
    **             01
    ***            012
    ****           0123
'''
m = 1
for r in range(4): # 外层循环次数（行数）
    for i in range(m): # 内层循环（每一行的个数）
                       # 可以考虑用 r + 1 而不是计数器
        print("*", end=" ")
    m += 1
    print()
