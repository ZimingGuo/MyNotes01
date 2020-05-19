# author: Ziming Guo
# time: 2020/2/4
'''
练习7：
在控制台中获取一个整数
如果是偶数，则为变量 state 赋值"偶数"
否则赋值"奇数"
'''
number = int(input("请输入一个整数："))
state = "偶数" if number % 2 == 0 else "奇数"
print(state)

# 用到了真值表达式
number = int(input("请输入一个整数："))
if number % 2:
    state = "奇数"
else:
    state = "偶数"
print(state)

# 用选择表达式 + 真值表达式
number = int(input("请输入一个整数："))
state = "奇数" if number % 2 else "偶数"
print(state)
