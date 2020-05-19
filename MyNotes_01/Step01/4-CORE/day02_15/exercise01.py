# author: Ziming Guo
# time: 2020/2/23
"""
    练习1：
    定义函数，根据年月日，返回星期数。
    即：随便给一个年月日，说出来是星期几
    0 "星期一"
    1 "星期二"
    2 "星期三"
     ...
     思路：年月日 --> 时间元组
          时间元组 --> 星期
          星期 --> 格式
"""
# 我的想法是：先写出来一个大函数，然后分解成小的函数
# 因为没有时间戳，所以只能用字符串获取时间元组

import time


def day_of_weeek():
    """
        获取星期数
    :return: 星期数
    """
    dict_weekday = {0: "一", 1: "二", 2: "三", 3: "四", 4: "五", 5: "六", 6: "日"}

    time_str = input("请输入日期，格式：年/月/日:")
    time_tuple = time.strptime(time_str, "%Y/%m/%d")
    # 也可以这样构建字符串："%d,%d,%d"%(year,month,day) # 作用是把后面的这三个变量插在前面的格式里面
    weekday = time_tuple[6]

    for key, value in dict_weekday.items():
        if key == weekday:
            print("今天是星期", value)


while True:
    day_of_weeek()
