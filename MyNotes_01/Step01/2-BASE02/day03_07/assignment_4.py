# author: Ziming Guo
# time: 2020/2/10
'''
    作业4：
        (扩展)方阵转置.（不用做成函数） # 方阵！
        提示：详见图片.

        这就是一个简单的算法
        解决这道题的过程就是逐条写出找规律的过程
        最后的代码不一样是正常的
        重要的是逻辑
'''
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

for a in range(len(list01)-1):
    for i in range(len(list01)-1-a):
        list01[a][i+1],list01[i+1][a] = list01[i+1][a],list01[a][i+1]

print(list01)

# # 边长为4（4-1）
# list01[0][1] # 2
# list01[1][0] # 5
#
# list01[0][2] # 3
# list01[2][0] # 9
#
# list01[0][3] # 4
# list01[3][0] # 13
# for i in range(len(list01)-1):
#     list01[0][i+1],list01[i+1][0] = list01[i+1][0],list01[0][i+1]
#
# # 边长为3（3-1）
# list01[1][2]
# list01[2][1]
#
# list01[1][3]
# list01[3][1]
# for m in range(len(list01)-2):
#     list01[1][m+2],list01[m+2][1] = list01[m+2][1],list01[1][m+2]
#
# # 边长为2（2-1）
# list01[2][3]
# list01[3][2]
# for n in range(len(list01)-3):
#     list01[2][n+3],list01[n+3][2] = list01[n+3][2],list01[2][n+3]

