# author: Ziming Guo
# time: 2020/2/4
'''
作业3：
在控制台中获取月份，显示季度，或者显示月份错误
'''
month = int(input("请输入月份："))
if month > 12 or month < 1:
    print("输入月份错误！")
elif month > 9:
    print("第四季度")
elif month > 6:
    print("第三季度")
elif month > 3:
    print("第二季度")
else:
    print("第一季度")
