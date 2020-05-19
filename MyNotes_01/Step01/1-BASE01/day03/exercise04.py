# author: Ziming Guo
# time: 2020/2/4
'''
练习4：
在控制台中分别录入4个数字
打印最大的数字
'''
number_1 = float(input("请输入数字1："))
number_2 = float(input("请输入数字2："))
number_3 = float(input("请输入数字3："))
number_4 = float(input("请输入数字4："))
max_number = 0

if number_1 >= number_2:
    max_number = number_1
else:
    max_number = number_2

if max_number < number_3:
    max_number = number_3

if max_number < number_4:
    max_number = number_4

print("最大的数为：" + str(max_number))
