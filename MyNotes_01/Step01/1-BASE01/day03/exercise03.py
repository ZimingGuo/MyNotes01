# author: Ziming Guo
# time: 2020/2/4
'''
练习3：
在控制台录入一个数字
在录入一个运算符（ + - * / ）
再录入一个数字
根据运算符进行计算
如果运算符不满足这四个要求，则显示"运算符有误"
'''
number_1 = float(input("请输入第一个数字："))
number_2 = float(input("请输入第二个数字："))
operator = input("请输入一个运算符号：")

if operator == "+":
    result = "运算结果为：" + str(number_1 + number_2)
elif operator == "-":
    result = "运算结果为：" + str(number_1 - number_2)
elif operator == "*":
    result = "运算结果为：" + str(number_1 * number_2)
elif operator == "/":
    if number_2 == 0:
        result = "除数不能为0"
    else:
        result = "运算结果为：" + str(number_1 / number_2)
else:
    result = "运算符输入错误！"

print(result)
