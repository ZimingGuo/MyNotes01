# author: Ziming Guo
# time: 2020/2/8
'''
    练习1：
    使用range生成1--10之间的数字
        1)将数字的平方存入list01中
        2)将list01中所有奇数存入list02
        3)将list01中所有偶数存入list03
        4)将list01中所有偶数大于5的数字增加1后存入list04
'''
list_original = []
list01 = []
list02 = []
list03 = []
list04 = []
for i in range(1, 11):
    list_original.append(i)
print(list_original)

# 平方变换
# for item in list_original:
#     list01.append(item ** 2)
list01 = [item ** 2 for item in list_original]
print(list01)

# 奇数
# for item in list_original:
#     if item % 2 == 1:
#         list02.append(item)
list02 = [item for item in list_original if item % 2 == 1]
print(list02)

# 偶数
# for item in list_original:
#     if item % 2 == 0:
#         list03.append(item)
list03 = [item for item in list_original if item % 2 == 0]
print(list03)

# 偶数大于5就加一
# for item in list_original:
#     if item % 2 == 0 and item > 5:
#         list04.append(item+1)
list04 = [item + 1 for item in list_original if item % 2 == 0 and item > 5]
print(list04)
