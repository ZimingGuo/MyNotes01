# author: Ziming Guo
# time: 2020/2/11
'''
    练习9：
#  练习:定义函数，根据小时，分钟，秒，计算总秒数.
#  要求：可以只计算小时-->秒
# 　　　可以只计算分钟-->秒
# 　　　可以只计算小时＋分钟-->秒
# 　　　可以只计算小时＋秒-->秒
'''


def count_second(second=0, minute=0, hour=0, day=0):
    sum_second = second + minute * 60 + hour * 60 ** 2 + day * 24 * 60 ** 2
    return sum_second


# get_second = int(input("请输入秒数："))
# get_minute = int(input("请输入分钟数："))
# get_hour = int(input("请输入小时数："))
# get_day = int(input("请输入天数："))
# count_second(second=get_second, minute=get_minute, hour=get_hour, day=get_day)

print(count_second(hour=2, day=1))
