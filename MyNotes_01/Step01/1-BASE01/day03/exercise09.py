# author: Ziming Guo
# time: 2020/2/4
'''
练习9：
使下列代码循环执行，按 e 键退出
并且调试程序
season = input("请输入一个季度：")
if season == "春":
    print("1月2月3月")
elif season == "夏":
    print("4月5月6月")
elif season == "秋":
    print("7月8月9月")
elif season == "冬":
    print("10月11月12月")
else:
    print("输入错误！")
'''
while True:
    season = input("请输入一个季度：")
    if season == "春":
        print("1月2月3月")
    elif season == "夏":
        print("4月5月6月")
    elif season == "秋":
        print("7月8月9月")
    elif season == "冬":
        print("10月11月12月")
    else:
        print("输入错误！")
    if input("按e键退出") == "e":
        break
