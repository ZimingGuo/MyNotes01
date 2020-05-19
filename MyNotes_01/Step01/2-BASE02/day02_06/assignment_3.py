# author: Ziming Guo
# time: 2020/2/9
'''
    作业3：
    将1970年到2050年中的闰年，存入列表．
'''
list_run_year = []
for year in range(1970, 2051):
    # 判断闰年方法：
    divided_4 = year % 4 == 0
    not_divided_100 = year % 100 != 0
    divided_400 = year % 400 == 0
    final_result = (divided_4 and not_divided_100) or (divided_400)
    if final_result == True:
        list_run_year.append(year)

print(list_run_year)

# 用列表推导式也可以

