# author: Ziming Guo
# time: 2020/2/2
'''
练习1：
交换两个量
'''
data01 = input("请输入一个变量data01：")
data02 = input("请输入另外一个变量data02：")

# 交换变量方法1 - 所有语言的通用思想
# temp = data01
# data01 = data02
# data02 = temp

# 交换变量方法2 - python 的独有思想，以后会经常用到
data01, data02 = data02, data01  # 另一种交换变量的方法（以后会经常遇到）

print("交换之后的变量data01是：" + data01)
print("交换之后的变量data02是：" + data02)
