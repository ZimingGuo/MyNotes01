# author: Ziming Guo
# time: 2020/2/5
'''
练习1：
在控制台中获取一个开始值，和一个结束值
将中间的数字打印出来
例如：开始3，结束10，打印4 5 6 7 8 9
'''
start_number = int(input("请输入一个开始值："))
final_number = int(input("请输入一个结束值："))

count = start_number
while count < final_number - 1:
    count += 1
    print(count)
