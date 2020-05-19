# author: Ziming Guo
# time: 2020/2/10
'''
练习5：
    定义函数，根据年月，计算有多少天，考虑闰年的情况（闰29天，平28天）

    在控制台获取一个月份
    打印天数，或者显示"输入有误"
    135781012——31天
    46911——30天
    2——28天
'''

# 不建议一个函数返回的数据有多种类型 不建议 不建议
#       这样会让调用者手足无措，不方便之后的操作
#       在别的语言里根本不可以这样，python里可以是因为python里的变量没有类型
#       可以用一种不可能的数据表示（None）


# 定义函数1-判断是否为闰年
def whether_run_years(year):
    """
    判断一个年份是否是闰年
    :param year: 要判断的年份
    :return:
    """
    # 能被4整除：
    divided_4 = year % 4 == 0
    # 不能被100整除：
    not_divided_100 = year % 100 != 0
    # 能被400整除：
    divided_400 = year % 400 == 0
    final_result = (divided_4 and not_divided_100) or (divided_400)
    return final_result
# 判断闰年的这一大串代码，建议拿出去，独立成一个函数
#   因为一个函数只能做一件事

# 定义函数2-判断有几天
def days_in_month(month,year):
    """
    输入月份和这个月份所在的年份，判断这个月有多少天
    :param month: 月份
    :param year: 年份
    :return: 天数
    """
    if month > 12 or month < 0:
        return 0            # 这里用 return 可以保证满足条件直接退出
                            #     不必担心程序继续向下做判断
                            # 而原来没有退出，会继续项下判断，所以用 elif 表示互斥性
    if month == 2:
        # if whether_run_years(year) == True:
        #     return 29
        # else:
        #     return 28
        # 上面的这一长段话也可以用 if 的条件表达式写, 四句话变成一句话
        return 29 if whether_run_years(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31

print(days_in_month(2,2019))

# 不建议一个函数返回的数据有多种类型 不建议 不建议
# 函数只做一件事，不一样的主题就建立新的函数，函数和函数之间可以相互调用



