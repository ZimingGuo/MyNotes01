# author: Ziming Guo
# time: 2020/2/8
'''
    练习3:
    在控制台中录入日期(月日)，计算这是这一年的第几天.
    例如：３月５日
         1月天数 + 2月天数 + 5

         5月8日
         1月天数 + 2月天数 +3月天数 + 4月天数+ 8
'''
# 方法1：索引
day01 = 0
input_month = int(input("请输入月份："))
input_day = int(input("请输入天："))
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
for i in range(0, input_month - 1):
    day01 += day_of_month[i]

day02 = input_day
print("一共%d天" % (day01 + day02))

# 方法2：切片
#   用切片的方法
total_day = sum(day_of_month[:input_month - 1])  # 但是你要知道，你这样切片出来的是个元组
print(total_day)
#   有意识的记住 sum 函数
