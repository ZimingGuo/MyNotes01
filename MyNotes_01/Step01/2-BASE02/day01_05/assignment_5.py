# author: Ziming Guo
# time: 2020/2/7
'''
作业5：
    彩票　双色球：
    红球:6个，1 -- 33 之间的整数   不能重复
    蓝球:1个，1 -- 16 之间的整数
    # 就是有7个数，6个1-33之间的数，一个1-16之间的数
    # 随机生成一个数，且不重复（用 in ）
    (2) 在控制台中购买一注彩票
    提示：
        "请输入第1个红球号码："
        "请输入第2个红球号码："
        "号码不在范围内"
        "号码已经重复"
        "请输入蓝球号码："
'''
list_ball = []
count = 0

# # 红球：
# for i in range(0, 6):
#     red01 = int(input("请输入第%d个红球号码：" % (i + 1)))
#     # ！先！判断是否在范围内
#     while red01 < 1 or red01 > 34:  # 像这种不知道要实现几次的操作就要用 while 来实现
#         red01 = input("号码不在范围内!重新输入：")
#     else:
#         # ！后！判断是否重复
#         while red01 in list_ball:
#             red01 = input("号码已经重复!重新输入：")
#         else:
#             list_ball.append(red01)

# # 我的红球方法2：
# while len(list_ball) < 6:
#     red = int(input("请输入第%d个红球号码：" % (count + 1)))
#     if red not in list_ball:
#         if 1 < red < 34:
#             list_ball.append(red)
#             count += 1
#         else:
#             print("号码不在范围内,重新输入!")
#     elif red in list_ball:
#         print("号码已经重复,重新输入!")

# 老师的红球方法：
#   此方法的优点：判断条件的时候是两个并列的条件
#   而不用把两个条件嵌套起来
while len(list_ball) < 6:
    red = int(input("请输入第%d个红球号码：" % (count + 1)))
    if red in list_ball:
        print("号码已经重复,重新输入!")
    elif red > 33 or red < 1:
        print("号码不在范围内,重新输入!")
    else:
        list_ball.append(red)
        count += 1

# 蓝球：
blue01 = int(input("请输入一个蓝球号码："))
while blue01 < 1 or blue01 > 16:
    blue01 = input("号码不在范围内!重新输入：")
else:
    list_ball.append(blue01)

print(list_ball)

# 经验：
#   在写条件的时候，尽量用并列的写法，而不是嵌套
#   并列：多个 if 并列 or 多个 while 并列
#   嵌套：while 里面有 if or if 里面有 while

