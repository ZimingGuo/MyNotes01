# author: Ziming Guo
# time: 2020/2/3
'''
作业7：
（扩展）在控制台中获取总秒数，计算几小时零几分钟零几秒
'''
total_second = int(input("请输入总秒数："))

second = total_second % 60
minute = total_second // 60 % 60
hour = total_second // 60 // 60

print("总共" + str(hour) + "小时" + str(minute) + "分钟" + str(second) + "秒")

# 取余表示的意思是：要剩下的部分
