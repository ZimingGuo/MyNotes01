# author: Ziming Guo
# time: 2020/2/23
'''
    计算活了多少秒 or 分钟
'''
import time

# def how_long_do_i_live():


def get_time_difference(year, month, day):
    time_tuple = time.strptime("%d/%d/%d" % (year, month, day), "%Y/%m/%d")
    start_second = time.mktime(time_tuple)  # 时间元组 --> 时间戳
    now_second = time.time()
    time_difference = now_second - start_second
    return time_difference


def transfer(total_second):
    total_minutes = total_second // 60
    total_hours = total_minutes // 60
    total_days = total_hours // 24
    return total_minutes, total_hours, total_days


def show_result(time_tuple):
    m = time_tuple[0]
    h = time_tuple[1]
    d = time_tuple[2]
    print("总分钟数为%d分钟，总小时数为%d小时，总天数为%d天。" % (m, h, d))


# 测试代码
total_seconds = get_time_difference(1997, 10, 23)
data_tuple = transfer(total_seconds)
show_result(data_tuple)
