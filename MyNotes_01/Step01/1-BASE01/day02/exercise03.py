# author: Ziming Guo
# time: 2020/2/2
'''
练习3：
获取秒；获取分钟；获取小时；获取天
计算有多少秒
'''
second = int(input("请输入秒数："))
minute = int(input("请输入分钟数："))
hour = int(input("请输入小时数："))
day = int(input("请输入天数："))

sum_second = second + minute * 60 + hour * 60 ** 2 + day * 24 * 60 ** 2
print("总共的秒数是：" + str(sum_second))

