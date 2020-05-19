# author: Ziming Guo
# time: 2020/2/5
'''
练习7：
    值得借鉴的思想：判断一个数字是否是素数
    在控制台中获取一个整数，判断是否为素数。
        素数:只能被１和自身整除的正数.
        思路：排除法,使用２到当前数字之间的正数判断，如果存在被整除，则不是素数.
         判断9：
            能否被2　--  8 之间的数字整除,其中3可以，所以不是素数.
         判断８:
            能否被2　--  7 之间的数字整除,其中2可以，所以不是素数.
         判断7:
            能否被2　--  6 之间的数字整除,其中没有，所以是素数.
'''

# 我的第一种方法：for
number = int(input("请输入一个数字："))
if number<=1:
    print("不是素数！")
else:
    for i in range(2, number):
        if number % i == 0:
            print("不是素数")
            break # 如果发现满足条件的数字，就不再判断后面的了
    else: # 表示：如果上面的条件都做完了还不满足，就执行下面语句
        print("是素数")

    # 通过调试发现，for 也可以和 else 和 break 一起使用
    # break 用于跳出 for 语句，有了 break 就不会进入 else 语句了
    # else 的作用是当条件不满足的时候需要执行的语句
    # for 语句在满足条件的情况下是一直在 else 之上一直循环的
    # break 和 else 适合搭配起来使用


# 我的第二种方法：while
m = 2
while m < number:
    if number % m == 0:
        print("不是素数")
        break
    elif number % m != 0:
        m += 1
else:
    print("是素数")

    # 总结经验：
    # while 语句在满足条件的情况下是一直在 else 之上一直循环的
    # break 和 else 适合搭配起来使用
