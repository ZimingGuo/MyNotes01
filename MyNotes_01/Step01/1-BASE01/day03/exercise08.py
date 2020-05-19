# author: Ziming Guo
# time: 2020/2/4
'''
练习8：
在控制台中录入一个年份
如果是闰年，给变量day赋值29
否则赋值28
'''
day = 0
year = int(input("请输入一个年份："))
# 能被4整除：
divided_4 = year % 4 == 0
# 不能被100整除：
not_divided_100 = year % 100 != 0
# 能被400整除：
divided_400 = year % 400 == 0

final_result = (divided_4 and not_divided_100) or (divided_400)

day = 29 if final_result == True else 28
print(day)
