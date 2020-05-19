# author: Ziming Guo
# time: 2020/2/9
'''
# 练习1:
    ["无忌","赵敏","周芷若"] -> {"无忌":2,"赵敏":2,"周芷若":3}
    原列表元素做键，元素的长度做值
'''
list01 = ["无忌", "赵敏", "周芷若"]
dict01 = {item: len(item) for item in list01}
print(dict01)

# 从不同的列表里面同时取出同位置的元素：用索引

# 需求：
# 字典如何根据value查找key
# 解决方案 1：键值互换
dict02 = {value: key for key, value in dict01.items()}
print(dict02)

# 此方法的缺点：如果 key 重复，交换有可能丢失数据(因为键相同时，新的值会覆盖旧的值)
# 如果需要保持所有数据：
list02 = [(value, key) for key, value in dict01.items()]
print(list02)
# 这种方法也是迫不得已，用列表套元组的方式来实现
# 只有元组和列表可以打破不能重复的规律

# 经验：字典和列表可以来回互换
