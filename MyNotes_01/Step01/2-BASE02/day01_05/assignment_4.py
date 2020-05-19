# author: Ziming Guo
# time: 2020/2/8
'''
作业4：
    彩票　双色球：
    红球:6个，1 -- 33 之间的整数   不能重复
    蓝球:1个，1 -- 16 之间的整数
    # 就是有7个数，6个1-33之间的数，一个1-16之间的数
    # 随机生成一个数，且不重复（用 in ）
    (1) 随机产生一注彩票[6个红球１个蓝球].
'''
import random

list01 = []
count = 0
# 想好这个地方用什么循环
#   用 for 循环是不太合适的，因为 for 循环是固定次数的
#   如果有重复的数字，总数就会比6少

while count < 6: # 也可以 while len(list01) < 6:
    red = random.randint(1, 33)
    if red not in list01:  # 判断这个数据是否在这个列表里面
        list01.append(red)
        count += 1

blue = random.randint(1, 16)
list01.append(blue)

print(list01)
