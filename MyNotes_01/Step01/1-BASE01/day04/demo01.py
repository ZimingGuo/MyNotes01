# author: Ziming Guo
# time: 2020/2/5
'''
猜数游戏 2.0
只能有三次机会，猜不对就游戏失败
'''
import random
random_number = random.randint(1, 100)

count = 0
while count<3:
    # 执行三次以内
    count += 1
    guess_number = int(input("请猜一个随机数："))
    if guess_number > random_number:
        print("猜大了,重新猜测")
    elif guess_number < random_number:
        print("猜小了,重新猜测")
    else:
        print("猜对了，共猜了" + str(count) + "次")
        break # 退出循环体，不会执行while的else语句
else: # 表示 while 的条件不满足
      # 执行了三次以上
    print("游戏失败！")