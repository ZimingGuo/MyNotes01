# author: Ziming Guo
# time: 2020/2/5
'''
练习3：
猜数字游戏
游戏运行产生一个1-100之间的随机数
让玩家反复猜测，知道猜对为止
提示：大了 or 小了 or 才多了，共猜了多少次
'''

import random
random_number = random.randint(1, 100)

# # 我的方法：
# guess_number = int(input("请猜一个随机数："))
# count = 1
#
# while guess_number != random_number:
#     # while 的作用是满足条件就执行，而不是满足条件就跳过
#     if guess_number > random_number:
#         print("猜大了,重新猜测")
#     elif guess_number < random_number:
#         print("猜小了,重新猜测")
#     count += 1
#     guess_number = int(input("请猜一个随机数："))
#
# print("猜对了，共猜了" + str(count) + "次")

# 老师的方法更好：
count = 0
while True:
    count += 1
    guess_number = int(input("请猜一个随机数："))
    if guess_number > random_number:
        print("猜大了,重新猜测")
    elif guess_number < random_number:
        print("猜小了,重新猜测")
    else:
        print("猜对了，共猜了" + str(count) + "次")
        break

# 宝贵经验：
# 老师方法的理论基础是
# if elif else 在使用中，一旦检测到满足 if 或 elif 的条件后
# 就会返回 True
# 如果都不满足，就会进入 else 且返回 False
# 所以才能用上述方法执行

# 总结：
# 满足 if 和 elif 的条件才会执行条件且返回 True
# 不满足就执行 else 且返回 False