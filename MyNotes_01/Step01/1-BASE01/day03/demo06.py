# author: Ziming Guo
# time: 2020/2/4
'''
    循环语句
        while 条件:
            循环体
'''
# 死循环
while True:
    usd = float(input("请输入美元："))
    print(usd * 6.9)
    if input("输入任意键退出"):
        break
