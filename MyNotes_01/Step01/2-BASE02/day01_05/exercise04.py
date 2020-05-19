# author: Ziming Guo
# time: 2020/2/7
"""
    练习4：
    １）:
        将列表[54,25,12,42,35,17]中，
        大于30的数字存入另外一个列表.
        并画出内存图.

    ２）：
        在控制台中录入５个数字，
        打印最大值（不适用max）. # 可以用到相互比较的方法
"""
'''
有个内存图，别忘了粘贴上面
'''
# 练习1：
list01 = [54, 25, 12, 42, 35, 17]
list02 = []
for item in list01: # 这句话的内存图很重要
                    # 这句话是把 list01 里面的每一个元素里所存储的东西给了 item
                    # 而不是把 list01 里面的每一个元素的地址给了 item
    if item > 30:
        list02.append(item)

print(list02)

# 练习2：
list03 = []
count01 = 1
count02 = 0
bigger = 0
while count01 < 6:
    number = input("请输入第%d个数字：" % (count01))
    list03.append(number)
    count01 += 1

# 想用这种相互比较的方法就要先假设第一个最大
#       精髓：先假设 先假设 先假设
bigger=list03[0]
# 假设第一个是最大的，从第二个开始进行比较
for i in range(1, len(list03)):
    if bigger < list03[i]:
        bigger = list03[i]
print(bigger)


# 再补充一点 break 的作用：
# 有了 break 之后，就会跳出循环，不会进入else语句，不然就会执行 else 语句

# 有这么一种情况，很适合用 while / for + else 语句：
    # 满足条件的时候执行语句，并且执行的语句里面有 if
        # 满足 if 语句就会 break 出 while / for 循环
        # 并且跳过 else 语句，因为 else 也算是循环的结构
        # 不满足 if 语句就会继续执行 while / for 循环
    # 当 while / for 语句都执行结束后，仍没有满足满足 if 语句的
    # 在结束循环语句之后会自动进入 else 语句
    # 执行完 else 里面的语句后向下执行
