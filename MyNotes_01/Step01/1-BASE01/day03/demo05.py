# author: Ziming Guo
# time: 2020/2/4
'''
真值表达式
    if 数据：
        语句
    本质就是使用 bool 函数操作数据

条件表达式
'''
# 1 真值表达式：
if 100:
    print("真值")

if bool(100):
    print("真值")
# 这两种写法表达的是一个意思

# 开发的时候经常这么写：因为方便
str_input = input("请输入：")
if str_input:
    print("输入的字符串不是空的")

# 2 条件表达式：有选择性的为变量进行赋值
sex = None
if input("请输入性别：") == "男":
    sex = 1
else:
    sex = 0
print(sex)

# 这两段代码的功能是一样的
sex = 1 if input("请输入性别：") == "男" else 0
print(sex)
