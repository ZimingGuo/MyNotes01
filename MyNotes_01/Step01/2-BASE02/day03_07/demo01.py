# author: Ziming Guo
# time: 2020/2/9
'''
    demo01：
      字典推导式：
'''
# 1 2 3 4 5 6 7 8 9 10 把这些数放在列表里 键是数本身 值是数的平方

dict01 = {}
for item in range(1, 11):
    dict01[item] = item ** 2

print(dict01)

# 推导式 1 ：
dict02 = {item: item ** 2 for item in range(1, 11)}
#   和列表推导式的差异是：方括号 和 冒号
print(dict02)

# 推导式 2 ：
# 只记录大于5的数字
dict01 = {}
for item in range(1, 11):
    if item > 5:
        dict01[item] = item ** 2

dict02 = {item: item ** 2 for item in range(1, 11) if item > 5}
print(dict02)
