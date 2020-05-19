# author: Ziming Guo
# time: 2020/2/4
'''
练习6：
在控制台获取一个月份
打印天数，或者显示"输入有误"
135781012——31天
46911——30天
2——28天
'''
month = int(input("请输入一个月份："))
if month > 12 or month < 0:
    print("输入错误！")
elif month == 2:
    print("这个月有28天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("这个月有30天")
else:
    print("这个月有31天")
