# author: Ziming Guo
# time: 2020/2/8
"""
    练习2:
    借助元组完成下列功能.
"""
# month = int(input("请输入月份："))
#
# if month < 1 or month > 12:
#     print("输入有误")
# elif month == 2:
#     print("２８天")
# elif month == 4 or month == 6 or month == 9\
#         or month == 11:
#     print("３０天")
# else:
#     print("３１天")

# 方式1：
tuple_30 = (4, 6, 9, 11)
tuple_31 = (1, 3, 5, 7, 8, 10, 12)
tuple_28 = (2)
# 其实上面的这些数据放在列表里面也可以
# 但是由于这些数据不会变化，放在元组里面节省空间

month = int(input("请输入月份："))
if month in tuple_30:
    print("30天")
elif month in tuple_31:
    print("31天")
elif month in tuple_28:
    print("28天")
else:
    print("输入错误！")

# 方式2：
# 将每个月的天数存入元组
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月份："))
print("%d天" % (day_of_month[month - 1]))

# 经验：
# 这是一种用容器统一管理数据的思想
