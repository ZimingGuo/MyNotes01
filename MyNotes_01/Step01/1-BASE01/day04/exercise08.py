# author: Ziming Guo
# time: 2020/2/5
'''
练习8：
    累加10-50之间个位不是2，5，9的整数
'''
sum_value = 0
for item in range(10, 51):
    # 运用的思想：
    # 想做到：个位不是259的数的累加
    # 可以先：个位是259的跳过
    if item % 10 == 2 or item % 10 == 5 or item % 10 == 9:
        continue
    sum_value += item
print(sum_value)
