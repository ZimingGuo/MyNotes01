# author: Ziming Guo
# time: 2020/2/5
'''
    demo02
    for：适合执行预定次数（已知次数）
    while：适合根据条件循环执行（未知次数）
'''
# for 语句就是让 for 里面的语句循环执行的

# for 变量 in 可迭代对象：
#     循环体

str01 = "我叫苏大强！"

# item 存储的是字符串的每个字符地址
for item in str01:
    print(item)

# 还可以用作整数生成器：range(开始值，结束值，间隔)
# for + range: 这种搭配更适合执行预定次数

for item in range(5):  # 01234
    print(item)

# 需求：折纸10次
thickness = 0.0001
for item in range(10):
    thickness += 2
