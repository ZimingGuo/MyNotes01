# author: Ziming Guo
# time: 2020/2/7
'''
作业3：
    连续获取字符，生成列表，以空字符串为结束
    计算列表中最小值(不使用min)
'''
list01 = []
while True:
    str01 = input("请输入一个数字：")
    if str01 == "":
        break
    list01.append(str01)
# 将所有获取的字符放入列表

min_list01 = list01[0]
for i in range(1, len(list01)):
    if int(min_list01) > int(list01[i]): # 这句if语句中一直进不来的原因是：
                                         # 一直比较的是字符串的编码值，而不是数字本身
        min_list01 = list01[i]
# 在列表里面依次比较，找出最小的元素
print(min_list01)
# 打印

# 经验：
#   在找几个数字的最大值 or 最小值的时候一定注意
#   字符串 & 整形的关系！